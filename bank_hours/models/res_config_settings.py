from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    overtime_multiplier = fields.Float(string="Overtime Multiplier", default=1.5, help="Multiplier for extra hours (e.g. 1.5 for 50% extra).")
    bank_hours_expiry_months = fields.Integer(string="Hours Expiry (Months)", default=12, help="Number of months before accumulated hours expire.")
    min_rest_hours = fields.Float(string="Minimum Rest Hours", default=12.0, help="Minimum rest hours required between shifts.")

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    overtime_multiplier = fields.Float(related='company_id.overtime_multiplier', readonly=False)
    bank_hours_expiry_months = fields.Integer(related='company_id.bank_hours_expiry_months', readonly=False)
    min_rest_hours = fields.Float(related='company_id.min_rest_hours', readonly=False)
