# models/product_template.py
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_motorcycle = fields.Boolean(string="Is Motorcycle")
    horsepower = fields.Float()
    top_speed = fields.Float()
    torque = fields.Float()
    battery_capacity = fields.Selection([
        ('xs', 'Small'),
        ('0m', 'Medium'),
        ('0l', 'Long'),
        ('xl', 'Extra Large')
    ], string="Battery Capacity")
    charge_time = fields.Float()
    range = fields.Float()
    curb_weight = fields.Float()
    make = fields.Char()
    model = fields.Char()
    year = fields.Char()

    @api.depends('is_motorcycle', 'year', 'make', 'model', 'name')
    def _compute_display_name(self):
        for product in self:
            if product.is_motorcycle:
                product.display_name = f"{product.year or ''} {product.make or ''} {product.model or ''}".strip()
            else:
                super(ProductTemplate, product)._compute_display_name()
