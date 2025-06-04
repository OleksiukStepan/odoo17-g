from odoo import models, fields, api


class CreateTaskWizard(models.TransientModel):
    _name = "helpdesk.create.task.wizard"
    _description = "Create Project Task from Helpdesk Ticket"

    helpdesk_ticket_id = fields.Many2one(
        "helpdesk.ticket", string="Helpdesk Ticket", required=True
    )
    name = fields.Char(string="Task Name", required=True)
    description = fields.Html(string="Description")
    partner_id = fields.Many2one("res.partner", string="Customer")
    user_ids = fields.Many2many("res.users", string="Assignees")
    tag_ids = fields.Many2many("project.tags", string="Tags")
    project_id = fields.Many2one("project.project", string="Project", required=True)
    stage_id = fields.Many2one(
        "project.task.type",
        string="Stage",
        required=True,
        domain="[('project_ids', 'in', project_id)]",
    )
    company_id = fields.Many2one("res.company", string="Company", required=True)

    @api.onchange("project_id")
    def _onchange_project_id(self):
        if self.project_id:
            self.stage_id = (
                self.project_id.type_ids[:1] if self.project_id.type_ids else False
            )

    def action_create_task(self):
        self.ensure_one()
        task_vals = {
            "name": self.name,
            "description": self.description,
            "partner_id": self.partner_id.id,
            "user_ids": [(6, 0, self.user_ids.ids)],
            "tag_ids": [(6, 0, self.tag_ids.ids)],
            "project_id": self.project_id.id,
            "stage_id": self.stage_id.id,
            "helpdesk_ticket_id": self.helpdesk_ticket_id.id,
            "company_id": self.company_id.id,
        }
        task = self.env["project.task"].create(task_vals)
        return {
            "type": "ir.actions.act_window",
            "res_model": "project.task",
            "res_id": task.id,
            "view_mode": "form",
            "target": "current",
            "default_company_id": self.company_id.id,
        }
