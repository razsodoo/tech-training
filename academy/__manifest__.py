{
    'name': 'Odoo Academy',
    'summary': """Module to handle Course and Sessions""",
    'description': """Module to handle:
        - Courses
        - Sessions
        - Attendees
    """,
    'license': 'OPL-1',
    'author': 'fsrs',
    'website': 'www.odoo.com',
    'category': 'Custom Modules/Tech Training',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'demo/academy_course_demo.xml',
        'views/academy_course_views.xml',
    ],
    'demo': [],
    'application': True,
}
