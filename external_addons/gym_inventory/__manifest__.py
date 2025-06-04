{
    "name": "Gym inventory",
    "version": "1.0",
    "depends": ["base", "mail", "gym"],
    "author": "Stepan Oleksiuk",
    "category": "Services",
    "description": "Gym inventory manager",
    "license": "LGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "views/gym_inventory_views.xml",
        "views/gym_inventory_menu.xml",
    ],
    "images": ["static/description/icon.png"],
    "application": True,
    "installable": True,
}
