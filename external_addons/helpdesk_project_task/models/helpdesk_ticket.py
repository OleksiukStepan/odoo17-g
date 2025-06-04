from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    can_create_task = fields.Boolean(
        compute="_compute_can_create_task",
        store=False
    )

    @api.depends()
    def _compute_can_create_task(self):
        for ticket in self:
            is_manager = ticket.env.user.has_group(
                "helpdesk.group_helpdesk_manager"
            )
            is_assigned = ticket.user_id.id == ticket.env.uid
            ticket.can_create_task = is_manager or is_assigned

    def action_create_project_task(self):
        self.ensure_one()
        return {
            "name": "Create Project Task",
            "type": "ir.actions.act_window",
            "res_model": "helpdesk.create.task.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_helpdesk_ticket_id": self.id,
                "default_name": f"Task from ticket: {self.name}",
                "default_description": self.description,
                "default_partner_id": self.partner_id.id,
                "default_company_id": self.company_id.id,
            },
        }

    def _can_create_task(self):
        self.ensure_one()
        return self.user_id == self.env.user or self.env.user.has_group(
            "helpdesk.group_helpdesk_manager"
        )
