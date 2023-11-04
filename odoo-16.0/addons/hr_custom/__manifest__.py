{
    'name': 'HR Custom Addon',
    'version': '1.0',
    'depends': ['base', 'hr', 'hr_recruitment'],
    'author': 'M. Kostka',
    'category': 'Human Resources',
    'description': 'Custom HR Addon with new fields',
    'data': [
        'views/hr_employee_view.xml',
    ],
    'installable': True,
}