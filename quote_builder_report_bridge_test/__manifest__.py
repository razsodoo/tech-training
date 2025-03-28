{
    'name': 'Custom Quote Report Extension',
    'version': '1.0',
    'summary': 'Allows custom reports to be used in place of the default Sale Order report.',
    'description': 'This module extends the standard Sale Order report by allowing users to select custom reports created with Odoo Studio.',
    'category': 'Sales',
    'author': 'RAZS',
    'license': 'LGPL-3',
    'support': 'ricardozs96@gmail.com',
    'depends': ['sale', 'base', 'sale_management'],
    'data': [
        'views/sale_order_form_view.xml',
        'views/report_saleorder.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
