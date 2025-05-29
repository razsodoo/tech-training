{
    'name': "academy_sale",
    'author': "Odoo, Inc.",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom Modules/Tech Training',
    'version': '0.1',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['academy', 'sale_management'],

    # always loaded
    'data': [
        'views/academy_course_views.xml'
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/academy_sale_demo.xml',
    ],

    'auto_install': True,
}
