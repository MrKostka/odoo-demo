from odoo import http
from odoo.http import request

class ApplicantController(http.Controller):
    @http.route('/case_study/applicant/mock', auth='public')
    def marek(self, **kw):
        return "<h1>Welcome in GB.</h1>"
        

    @http.route('/case_study/applicant/get', type='json', auth='public', methods=['POST'])
    def create_applicant(self, **kwargs):
        # Extract data from the JSON request
        name = kwargs.get('name')
        phone = kwargs.get('phone')
        email = kwargs.get('email')
        gender = kwargs.get('gender')
        api_id = kwargs.get('api_id')

        # Create a new applicant record
        applicant = request.env['hr.applicant'].create({
            'name': name,
            'phone': phone,
            'email_from': email,
            'gender': gender,
            'job_id': request.env['hr.job'].search([('api_id', '=', api_id)], limit=1),
        })

        print(applicant)

        return {
            'success': True,
            'message': 'Applicant created successfully.',
            'applicant_id': applicant.id,
        }