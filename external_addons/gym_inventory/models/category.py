from odoo import fields, models


class GymInventoryCategory(models.Model):
    _name = "gym.inventory.category"
    _description = "Inventory Category"
    _inherit = ["mail.thread", "mail.activity.mixin"]


    name = fields.Char(required=True)
