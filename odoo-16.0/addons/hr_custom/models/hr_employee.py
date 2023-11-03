from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # _name = "hr_custom.employee"

    i_love_gb = fields.Boolean(string="I Love GB")

    # define new relation name and better column names 
    # and I think you need a new category model because this one is used for employee category, may be it's better to create hr.student.category table I don't know it's up to you
    category_ids = fields.Many2many(
      'hr.employee.category', 'category_id',
      string='Tags')