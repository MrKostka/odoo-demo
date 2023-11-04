
import base64

from odoo import models, fields, api
from odoo.exceptions import ValidationError

from xlrd import open_workbook
from io import BytesIO
class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    

    # 1. task
    i_love_gb = fields.Boolean(string="I Love GB")
    employee_contacts = fields.Binary(string="Employee Contacts")

    tax = fields.Integer(string="Tax")
    salary = fields.Integer(string="Salary")
    total_salary = fields.Integer(string="Total Salary", compute='_compute_total_salary')    

    special_phone = fields.Char(related='phone', string="Special Phone")

    # 2. task
    employee_number = fields.Char(string="Employee Number", required=True, tracked=True, unique=True)
    
    # I think I need a new categories field cause of error I faced to with them
    category_ids = fields.Many2many('hr.employee.category', 'category_id', string='Tags')
    
    salary._description = {
        'en_US': 'Monthly Salary',
        'fr_FR': 'Salaire mensuel',
        'es_ES': 'Salario mensual',
    }

    tax._description = {
        'en_US': 'Tax Amount',
        'fr_FR': "Montant de l'impôt",
        'es_ES': 'Cantidad de impuestos',
    }
    
    @api.depends('salary', 'tax')
    def _compute_total_salary(self):
        for record in self:
            record.total_salary = record.salary + record.tax

    # I did not find better solution for ,save action' - I see Save manually button but can not attach to it
    @api.constrains('special_phone')
    def _check_empty_field(self):
        for record in self:
            record.special_phone = "0901123456" if not record.special_phone else record.special_phone
    
    def action_send_mail(self):
        for record in self:
            if not record.employee_contacts:
                raise ValidationError("No Excel file found in the binary field")
            
            excel_content = record.employee_contacts

            try:
                inputx = BytesIO()
                inputx.write(base64.decodestring(excel_content))
                book = open_workbook(file_contents=inputx.getvalue())
            except TypeError as e:
                raise ValidationError(u'ERROR: {}'.format(e))
            sheet = book.sheets()[0]

            for i in range(sheet.nrows):
                address = sheet.cell(i, 0).value
                subject = sheet.cell(i, 1).value

                MailMail = self.env['mail.mail']
                email_values = {
                    'subject': subject,
                    'email_to': address,
                    'body_html': "Welcome in GymBeam",
                }

                # Send the email - yeah this is pity but I have lack of knowledge for mailing
                mail_id = MailMail.create(email_values)
                mail_id.send()

