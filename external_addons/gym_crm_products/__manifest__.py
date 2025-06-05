{
    "name": "CRM Gym Products",
    "version": "1.0",
    "depends": ["base", "mail", "crm", "gym_inventory"],
    "author": "Stepan Oleksiuk",
    "category": "Sales",
    "description": "Allow CRM Leads to add gym inventory as products.",
    "license": "LGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "views/crm_lead_views.xml",
        "views/product_package_views.xml",
        "views/add_package_wizard_views.xml",
    ],
    "application": False,
    "installable": True,
}
