from odoo import models, fields

class HrJob(models.Model):
    _inherit = 'hr.job'

    api_id = fields.Char(string="API ID", required=True)