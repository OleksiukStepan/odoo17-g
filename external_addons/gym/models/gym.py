from odoo import fields, models, api


class Gym(models.Model):
    _name = "gym.gym"
    _description = "Gym"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Gym name", required=True, tracking=True)
    location = fields.Char("Location", tracking=True)
