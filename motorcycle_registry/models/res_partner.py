from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_new_customer = fields.Boolean(
        string="Is New Motorcycle Customer", compute="_compute_is_new_customer", store=False
    )

    def _compute_is_new_customer(self):
        for partner in self:
            domain = [
                ('partner_id', '=', partner.id),
                ('state', 'in', ['sale', 'done']),
                ('order_line.product_id.product_tmpl_id.is_motorcycle', '=', True)
            ]
            previous_orders = self.env['sale.order'].search(domain, limit=1)
            partner.is_new_customer = not bool(previous_orders)
