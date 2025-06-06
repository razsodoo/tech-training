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
    name = fields.Char(compute='_compute_name', readonly=False, store=True)

    @api.model_create_multi
    def create(self, vals_list):
        motorcycle_category = self.env.ref('motorcycle_registry.product_category_motorcycle', raise_if_not_found=False)
        for vals in vals_list:
            if vals.get('is_motorcycle') and not vals.get('categ_id') and motorcycle_category:
                vals['categ_id'] = motorcycle_category.id
        return super().create(vals_list)

    @api.onchange('is_motorcycle')
    def _onchange_is_motorcycle_set_category(self):
        motorcycle_category = self.env.ref('motorcycle_registry.product_category_motorcycle', raise_if_not_found=False)
        if self.is_motorcycle and motorcycle_category and self.categ_id != motorcycle_category:
            self.categ_id = motorcycle_category
                
    @api.depends('is_motorcycle', 'make', 'model', 'year')
    def _compute_name(self):
        for rec in self:
            if rec.is_motorcycle:
                # Computamos el nombre: "year make model"
                name_parts = [rec.year or '', rec.make or '', rec.model or '']
                rec.name = ' '.join(filter(None, name_parts)).strip()
            else:
                # Si no es motocicleta, respetamos el valor previo (deja vacío si no hay ninguno)
                if not rec.name:
                    rec.name = ''
                    
    @api.depends('is_motorcycle', 'year', 'make', 'model', 'name')
    def _compute_display_name(self):
        for product in self:
            if product.is_motorcycle:
                product.display_name = f"{product.year or ''} {product.make or ''} {product.model or ''}".strip()
            else:
                super(ProductTemplate, product)._compute_display_name()
