{
    'name': 'Gym Membership',
    'version': '17.0.1.0.0',
    'summary': 'Manage gym memberships, clients, and subscriptions',
    'description': """
        This module allows you to manage gym memberships,
        including subscription types, client data, trainers,
        and progress tracking.
    """,
    'category': 'Services',
    'author': 'Stepan Oleksiuk',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/gym_membership_views.xml',
        'views/gym_membership_menu.xml',
    ],
    "images": ["static/description/icon.png"],
    'access': ['security/ir.model.access.csv'],
    'application': True,
    'installable': True,
    'auto_install': False,
}
