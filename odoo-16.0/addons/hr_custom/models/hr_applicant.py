
from odoo import models, fields

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    # 2. task
    employee_number = fields.Char(string="Employee Number", required=True, tracked=True, unique=True)