from odoo import models, fields, api


class CrmLeadAddPackageWizard(models.TransientModel):
    _name = "crm.lead.add.package.wizard"
    _description = "Add Product Package to Lead"

    lead_id = fields.Many2one(
        "crm.lead",
        string="Lead",
        required=True,
    )
    package_id = fields.Many2one(
        "crm.product.package",
        string="Package",
        required=True,
        domain="["
               "'|',"
               "('expiration_date','=',False),"
               "('expiration_date','>=',context_today())"
               "]"
    )
    line_ids = fields.One2many(
        "crm.lead.add.package.wizard.line",
        "wizard_id",
        string="Products",
    )

    @api.onchange("package_id")
    def _onchange_package_id(self):
        if self.package_id:
            lines = []
            for pkg_line in self.package_id.package_line_ids:
                lines.append(
                    (
                        0,
                        0,
                        {
                            "inventory_id": pkg_line.inventory_id.id,
                            "quantity": pkg_line.quantity,
                            "price_unit": pkg_line.price_unit,
                        },
                    )
                )
            self.line_ids = lines

    def action_add_to_lead(self):
        for line in self.line_ids:
            self.env["crm.lead.inventory.line"].create(
                {
                    "lead_id": self.lead_id.id,
                    "inventory_id": line.inventory_id.id,
                    "quantity": line.quantity,
                    "price_unit": line.price_unit,
                    "package_id": self.package_id.id,
                }
            )

        if self.package_id and self.package_id.tag_ids:
            lead_tags = (
                self.lead_id.tag_ids.ids
                if self.lead_id.tag_ids
                else []
            )
            package_tags = self.package_id.tag_ids.ids
            new_tags = list(set(lead_tags) | set(package_tags))
            self.lead_id.write({"tag_ids": [(6, 0, new_tags)]})


class CrmLeadAddPackageWizardLine(models.TransientModel):
    _name = "crm.lead.add.package.wizard.line"
    _description = "Wizard Line for Adding Product Package to Lead"

    wizard_id = fields.Many2one(
        "crm.lead.add.package.wizard",
        required=True,
        ondelete="cascade",
    )
    inventory_id = fields.Many2one(
        "gym.inventory",
        string="Product",
        required=True
    )
    quantity = fields.Integer(string="Quantity", default=1)
    price_unit = fields.Float(string="Unit Price")
