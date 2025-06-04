from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    is_trainer = fields.Boolean(string="Is Trainer")
