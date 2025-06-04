{
    "name": "Helpdesk Project Task",
    "version": "1.0",
    "category": "Services/Helpdesk",
    "summary": "Create Project Tasks from Helpdesk Tickets",
    "description": """
        This module allows creating project tasks directly from helpdesk tickets.
        Features:
        - Create project tasks from helpdesk tickets
        - Transfer ticket information to tasks
        - Link tasks back to tickets
    """,
    "author": "Stepan Oleksiuk",
    "depends": [
        "base",
        "helpdesk",
        "project",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/create_task_wizard_views.xml",
        "views/helpdesk_ticket_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}
