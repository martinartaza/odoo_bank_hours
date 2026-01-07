from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    @api.model_create_multi
    def create(self, vals_list):
        attendances = super(HrAttendance, self).create(vals_list)
        for attendance in attendances:
            if attendance.check_out and attendance.check_in:
                self._process_bank_hours(attendance)
        return attendances

    @api.constrains('check_in', 'check_out', 'employee_id')
    def _check_min_rest_time(self):
        for attendance in self:
            if not attendance.check_in or not attendance.employee_id:
                continue

            # Get config
            min_rest = attendance.employee_id.company_id.min_rest_hours
            if not min_rest:
                continue
                
            # Find last attendance
            last_attendance = self.search([
                ('employee_id', '=', attendance.employee_id.id),
                ('check_out', '<', attendance.check_in),
                ('id', '!=', attendance.id)
            ], order='check_out desc', limit=1)
            
            if last_attendance:
                delta = attendance.check_in - last_attendance.check_out
                # Delta is timedelta
                hours_diff = delta.total_seconds() / 3600.0
                if hours_diff < min_rest:
                    raise models.ValidationError(
                        f"Minimum rest time not respected! Required: {min_rest}h, Actual: {hours_diff:.2f}h."
                    )
                    
    def write(self, vals):
        # Proceed with standard write
        res = super(HrAttendance, self).write(vals)
        
        # Logic triggered only when check_out is set/changed
        if 'check_out' in vals:
            for attendance in self:
                if attendance.check_out and attendance.check_in:
                    self._process_bank_hours(attendance)
        return res

    def _process_bank_hours(self, attendance):
        employee = attendance.employee_id
        company = employee.company_id
        
        # skip if no calendar
        if not employee.resource_calendar_id:
            return

        # Calculate actual worked hours
        # Odoo stores worked_hours as float (e.g. 8.5)
        worked_hours = attendance.worked_hours
        
        # Calculate expected hours for that day
        # We assume the user checked in/out on the same day or shift logic applies
        # Simplification: get expected hours for the interval
        expected_hours = employee.resource_calendar_id.get_work_hours_count(
            attendance.check_in, 
            attendance.check_out
        )
        
        # Calculate delta
        delta = worked_hours - expected_hours
        
        # If extra hours
        if delta > 0.01: # tolerance
            multiplier = company.overtime_multiplier or 1.0
            bank_hours = delta * multiplier
            
            # Create Allocation (Accrual)
            # We need a Time Off Type for "Bank Hours". 
            # ideally this should be a setting, but for now we search or create one named "Bank of Hours"
            leave_type = self.env['hr.leave.type'].search([('name', '=', 'Bank of Hours')], limit=1)
            if not leave_type:
                # Should be created in data/ or manually. We'll skip or log warning.
                # For this proof of concept, we can try to find 'Compensatory Days'
                leave_type = self.env['hr.leave.type'].search([('name', 'ilike', 'Compensatory')], limit=1)
            
            if leave_type:
                # Calculate validity
                validity_months = company.bank_hours_expiry_months or 12
                date_to = date.today() + relativedelta(months=validity_months)
                
                # Create allocation
                self.env['hr.leave.allocation'].create({
                    'name': f'Overtime: {attendance.check_in.date()} ({delta:.2f}h x {multiplier})',
                    'employee_id': employee.id,
                    'holiday_status_id': leave_type.id,
                    'number_of_days': bank_hours / (employee.resource_calendar_id.hours_per_day or 8.0), # allocation is usually in days for Odoo < 17 or hours depending on config
                    # Odoo 17: Allocation duration_type can be 'hours'
                    'allocation_type': 'regular', 
                    'state': 'confirm', # Draft -> method to confirm?
                    'date_from': date.today(),
                    'date_to': date_to,
                })

            # Create Historial Log (always, regardless of leave_type)
            self.env['bank.hours.log'].create({
                'employee_id': employee.id,
                'company_id': company.id,
                'attendance_id': attendance.id,
                'date': attendance.check_in.date(),
                'worked_hours': worked_hours,
                'expected_hours': expected_hours,
                'delta_hours': delta,
                'multiplier': multiplier,
                'bank_hours': bank_hours,
            })

