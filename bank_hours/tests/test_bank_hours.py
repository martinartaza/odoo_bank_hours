from odoo.tests.common import TransactionCase
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

class TestBankHours(TransactionCase):

    def setUp(self):
        super(TestBankHours, self).setUp()
        self.Attendance = self.env['hr.attendance']
        self.Employee = self.env['hr.employee']
        self.LeaveType = self.env['hr.leave.type']
        
        # Use the Leave Type created by the module data
        self.bank_leave_type = self.env.ref('bank_hours.holiday_status_bank_hours')
        
        # Create an Employee with a standard 40h calendar
        self.employee = self.Employee.create({
            'name': 'Juan Test',
            'company_id': self.env.company.id,
        })
        
        # Configure Company
        self.env.company.overtime_multiplier = 1.5
        self.env.company.bank_hours_expiry_months = 6

    def test_overtime_allocation(self):
        """ Test that 2 hours overtime creates 3 hours allocation (1.5x) """
        
        # Simulate Check In at 08:00
        check_in = datetime.now().replace(hour=8, minute=0, second=0)
        # Check Out at 18:00 (10 hours work)
        # Assuming standard day is 8 hours (08:00-12:00, 13:00-17:00) 
        # But this depends on the default calendar which is usually Monday-Friday 8-12, 13-17.
        # So 8 to 18 is 2 hours overtime? 
        # (8-12=4) + (13-18=5) = 9 hours worked. Standard is 8. Overtime = 1.
        # Let's try 08:00 to 20:00 (12 hours span). Lunch 1 hour?
        # Better: let's treat the calendar as "Resource Calendar".
        # Odoo's test calendar usually has 8 hours/day.
        
        check_out = check_in + timedelta(hours=11) # 11 hours duration (e.g. 8 to 19)
        # If lunch is 1 hour, worked is 10. Expected is 8. Overtime = 2.
        # 2 * 1.5 = 3 hours allocation.
        
        attendance = self.Attendance.create({
            'employee_id': self.employee.id,
            'check_in': check_in,
            'check_out': check_out,
        })
        
        # Search for allocation
        allocation = self.env['hr.leave.allocation'].search([
            ('employee_id', '=', self.employee.id),
            ('holiday_status_id', '=', self.bank_leave_type.id)
        ], limit=1)
        
        self.assertTrue(allocation, "Allocation should be created")

    def test_min_rest_time_constraint(self):
        """ Test that check-in too early raises ValidationError """
        self.env.company.min_rest_hours = 12.0
        
        # Shift 1: Yesterday 08:00 - 18:00
        check_in_1 = datetime.now() - timedelta(days=1, hours=10) # Yesterday 
        check_out_1 = check_in_1 + timedelta(hours=10)
        
        self.Attendance.create({
            'employee_id': self.employee.id,
            'check_in': check_in_1,
            'check_out': check_out_1,
        })
        
        # Shift 2: Today 02:00 (Only 8 hours rest instead of 12)
        # check_out_1 was at (Now - 24 + 10 = Now - 14h)
        # We want to try checking in at Now - 6h. Gap = 8h.
        
        check_in_2 = check_out_1 + timedelta(hours=8)
        
        with self.assertRaises(Exception): # ValidationError is bubbled up usually
            self.Attendance.create({
                'employee_id': self.employee.id,
                'check_in': check_in_2,
                'check_out': False,
            })

