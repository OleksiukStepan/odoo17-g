from odoo import api, fields, models, _


class CrmLead(models.Model):
    _inherit = "crm.lead"

    inventory_line_ids = fields.One2many(
        "crm.lead.inventory.line",
        "lead_id",
        string="Inventory Lines",
    )
    has_expired_package = fields.Boolean(
        compute="_compute_expired_package_status"
    )
    expired_package_message = fields.Char(
        compute="_compute_expired_package_status"
    )

    def open_add_package_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "crm.lead.add.package.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_lead_id": self.id,
            },
        }

    @api.depends(
        "inventory_line_ids"
    )
    def _compute_expired_package_status(self):
        today = fields.Date.context_today(self)

        for lead in self:
            expired_present = False
            message = ""
            for line in lead.inventory_line_ids:
                pkg = line.package_id
                if (
                    not pkg
                    or not pkg.expiration_date
                    or pkg.expiration_date >= today
                ):
                    continue
                expired_present = True
                if not lead.stage_id.is_won:
                    message = _(
                        "Attention! Some products have been added "
                        "from a package that has expired!"
                    )
                break

            lead.has_expired_package = expired_present
            lead.expired_package_message = message
