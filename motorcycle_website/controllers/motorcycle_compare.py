# controllers/motorcycle_compare.py
from odoo import http
from odoo.http import request

class MotorcycleCompare(http.Controller):

    @http.route('/compare', type='http', auth='public', website=True)
    def compare_motorcycles(self, **kwargs):
        motorcycles = request.env['product.template'].sudo().search([
            ('detailed_type', '=', 'motorcycle')
        ])
        return request.render('motorcycle_website.compare_template', {
            'motorcycles': motorcycles
        })