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
        'data/academy_session_sequence.xml',
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        'views/academy_course_views.xml',
        'views/academy_session_views.xml',
        'views/academy_menu_items.xml',
    ],
    'demo': [
        'demo/course_demo.xml',
        'demo/session_demo.xml',
    ],
    'application': True,
}
