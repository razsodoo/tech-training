{
    'name': 'Motorcycle Registry',
    'summary': "Manage Registration of Motorcycles",
    'description': """Motorcycle Registry
    This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycle of the brand.""",
    'license': 'OPL-1',
    'author': 'razsodoo',
    'version': '0.0.1',
    'website': 'www.github.com/razsodoo/tech-training',
    'category': 'Kawiil/Custom Modules',
    'depends': ['base','contacts','stock', 'sale_management', 'product'],
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        'data/motorcycle_registry_sequence.xml',
        'data/product_category.xml',
        'data/pricelist_data.xml',
        "views/motorcycle_registry_menu.xml",
        "views/motorcycle_registry_view.xml",
        "views/product_template_motorcycle_form_view.xml",
        "views/product_template_search_view.xml",
        "views/sale_views.xml",
    ],
    'demo': [
        'demo/motorcycle_registry_demo.xml',
        'demo/motorcycle_product_demo.xml',
    ],
    'application': True,
}
