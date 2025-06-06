import random
import string
from odoo import models, fields, api

class StockLot(models.Model):
    _inherit = 'stock.lot'

    name = fields.Char(string="Serial Number", readonly=True, required=True, copy=False, default='/')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            product_id = vals.get('product_id')
            if product_id:
                product = self.env['product.product'].browse(product_id)
                if product and product.product_tmpl_id.is_motorcycle and (not vals.get('name') or vals['name'] == '/'):
                    vals['name'] = self._generate_vin()
        return super().create(vals_list)

    def _generate_vin(self):
        letters = string.ascii_uppercase
        digits = string.digits
        alphanum = letters + digits

        part1 = ''.join(random.choices(letters, k=2))
        part2 = ''.join(random.choices(digits, k=2))
        part3 = ''.join(random.choices(alphanum, k=2))
        part4 = ''.join(random.choices(digits, k=5))

        vin = f"{part1}{part2}{part3}{part4}"
        return vin
