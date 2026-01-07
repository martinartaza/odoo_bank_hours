from odoo import models, fields, api

class BankHoursLog(models.Model):
    _name = 'bank.hours.log'
    _description = 'Bank of Hours Log'
    _order = 'date desc, id desc'

    employee_id = fields.Many2one('hr.employee', string="Employee", required=True, index=True)
    company_id = fields.Many2one('res.company', string="Company", required=True, default=lambda self: self.env.company)
    attendance_id = fields.Many2one('hr.attendance', string="Attendance Reference", ondelete='set null')
    date = fields.Date(string="Date", default=fields.Date.context_today, required=True, index=True)
    
    worked_hours = fields.Float(string="Worked Hours")
    expected_hours = fields.Float(string="Expected Hours")
    delta_hours = fields.Float(string="Overtime (Raw)")
    multiplier = fields.Float(string="Multiplier")
    bank_hours = fields.Float(string="Bank Hours (Final)")
    
    # Fields for grouping and filtering
    month = fields.Char(string="Month", compute='_compute_month', store=True, index=True)
    year = fields.Integer(string="Year", compute='_compute_month', store=True, index=True)
    month_year = fields.Char(string="Month/Year", compute='_compute_month', store=True, index=True)
    
    name = fields.Char(string="Description", compute='_compute_name', store=True)

    @api.depends('date')
    def _compute_month(self):
        for record in self:
            if record.date:
                record.month = record.date.strftime('%B')  # Full month name
                record.year = record.date.year
                record.month_year = record.date.strftime('%Y-%m')  # Format: YYYY-MM
            else:
                record.month = False
                record.year = False
                record.month_year = False

    def _compute_name(self):
        for record in self:
            record.name = f"{record.employee_id.name} - {record.date} ({record.bank_hours}h)"
