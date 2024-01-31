from odoo import models, fields

class MeuPrimeiroModulo(models.Model):
    _name = 'meu.primeiro.modelo'
    _description = 'meu primeiro modelo criado no odoo'

    campo1 = fields.Integer(string="Campo 1")

    