from odoo import fields, models


class CrmProductPackage(models.Model):
    _name = "crm.product.package"
    _description = "CRM Product Package"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Package Name", required=True, tracking=True)
    package_line_ids = fields.One2many(
        "crm.product.package.line",
        "package_id",
        string="Products",
        tracking=True,
    )
    expiration_date = fields.Date(string="Expiration Date", tracking=True)
    tag_ids = fields.Many2many(
        "crm.tag",
        string="Tags",
        tracking=True,
    )

    def copy(self, default=None):
        if default is None:
            default = {}
        default['name'] = f"{self.name} (Copy)"
        return super().copy(default)


class CrmProductPackageLine(models.Model):
    _name = "crm.product.package.line"
    _description = "CRM Product Package Line"

    package_id = fields.Many2one(
        "crm.product.package",
        string="Package",
        required=True,
        ondelete="set null",
        tracking=True,
    )
    inventory_id = fields.Many2one(
        "gym.inventory", string="Product", required=True, tracking=True
    )
    quantity = fields.Integer(string="Quantity", default=1, tracking=True)
    price_unit = fields.Float(string="Unit Price", tracking=True)
