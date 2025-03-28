from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    report_id = fields.Many2one(
        "ir.actions.report",
        string="Custom Report",
        domain="[('model', '=', 'sale.order')]",
        help="Select a custom report to replace the default Sale Order report.",
    )
