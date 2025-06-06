from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def apply_motorcycle_discount(self):
        # Buscamos la pricelist creada
        pricelist = self.env.ref('motorcycle_registry.motorcycle_discount_pricelist')
        self.write({'pricelist_id': pricelist.id})
        self.action_update_prices()
        
