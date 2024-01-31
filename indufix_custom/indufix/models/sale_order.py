from odoo import models, fields

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    campo1 = fields.Integer(string="Campo 1")

    