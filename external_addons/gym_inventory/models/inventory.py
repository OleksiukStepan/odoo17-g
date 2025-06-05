from odoo import fields, models, api
from odoo.exceptions import ValidationError


class GymInventory(models.Model):
    _name = "gym.inventory"
    _description = "Gym inventory"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Inventory name", required=True, tracking=True)
    description = fields.Text(tracking=True)
    brand = fields.Char(string="Brand", tracking=True)
    safe_level = fields.Selection([
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High")
    ], string="Safe level", tracking=True)
    weight_kg = fields.Float(
        string="Weight(kg)",
        tracking=True,
    )
    weight_ton = fields.Float(
        string="Weight(ton)",
        store=True,
        tracking=True,
    )
    category_id = fields.Many2one(
        "gym.inventory.category",
        string="Category",
        tracking=True,
    )
    gym_id = fields.Many2one(
        "gym.gym",
        string="Gym",
        tracking=True,
    )
    article = fields.Char(string="Article", required=True, tracking=True)
    image = fields.Binary(string="Image", attachment=False)

    # ("constraint_name", "SQL condition", "Error message")
    _sql_constraints = [(
        "unique_article_code",
        "unique(article)",
        "Article code must be unique"
    )]


    @api.onchange("weight_kg")
    def _onchange_weight_kg(self):
        for rec in self:
            if rec.weight_kg:
                rec.weight_ton = rec.weight_kg / 1000


    @api.onchange("weight_ton")
    def _onchange_weight_ton(self):
        for rec in self:
            if rec.weight_ton:
                rec.weight_kg = rec.weight_ton * 1000


    @api.constrains("weight_kg", "weight_ton")
    def _check_weight_positive(self):
        for rec in self:
            if rec.weight_kg < 0:
                raise ValidationError("Weight cannot be negative.")


    def name_get(self):
        return [(rec.id, f"{rec.name} ({rec.brand})") for rec in self]
