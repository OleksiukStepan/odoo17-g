from odoo import fields, models, api


class CrmLeadInventoryLine(models.Model):
    _name = "crm.lead.inventory.line"
    _description = "Inventory Item in CRM Lead"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    lead_id = fields.Many2one(
        "crm.lead",
        required=True,
        ondelete="cascade",
        tracking=True,
    )
    inventory_id = fields.Many2one(
        "gym.inventory",
        required=True,
        tracking=True,
    )
    quantity = fields.Integer(
        default=1,
        tracking=True,
    )
    price_unit = fields.Float(
        tracking=True,
    )
    subtotal = fields.Float(compute="_compute_subtotal", store=True)
    package_id = fields.Many2one(
       "crm.product.package",
       string="Product Package",
       tracking=True,
    )

    @api.depends("quantity", "price_unit")
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.quantity * rec.price_unit
