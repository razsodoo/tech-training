{
    'name': 'Custom Quote Report Extension',
    'version': '1.0',
    'summary': 'Allows custom reports to be used in place of the default Sale Order report.',
    'description': """This module extends the standard Sale Order report by allowing users to select custom reports created with Odoo Studio.
    
    How to use: https://drive.google.com/file/d/1PNZv8RA0KGT4a8981Zti589CYtw-RlQQ/view?usp=sharing""",
    'category': 'Sales',
    'author': 'RAZS',
    'license': 'OPL-1',
    'price': 15,
    'currency': 'USD',
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
