from odoo import fields, models


class GymMembership(models.Model):
    _name = "gym.membership"
    _description = "Gym Membership"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Membership name", required=True, tracking=True)
    price = fields.Float(string="Price", required=True, tracking=True)
    start_date = fields.Date(string="Start date", tracking=True)
    end_date = fields.Date(string="End date", tracking=True)
    membership_type = fields.Selection([
        ("personal", "Personal"),
        ("group", "Group")
    ], string="Type", required=True, tracking=True)
    status = fields.Selection([
        ("active", "Active"),
        ("expired", "Expired"),
        ("cancelled", "Cancelled")
    ], string="Status", default="active", tracking=True)
    partner_id = fields.Many2one(
        "res.partner",
        string="Customer",
        required=True,
        tracking=True,
    )
    trainer_id = fields.Many2one(
        "res.partner",
        string="Trainer",
        domain="[('is_trainer','=',True)]",
        tracking=True,
    )
    description = fields.Text(string="Description", tracking=True)
    image_ids = fields.One2many(
        "gym.membership.image",
        "membership_id",
        string="Photos",
        tracking = True,
    )
    create_date = fields.Datetime(string="Created On", readonly=True)


class GymMembershipImage(models.Model):
    _name = "gym.membership.image"
    _description = "Gym Membership Image"

    membership_id = fields.Many2one(
        "gym.membership",
        string="Membership",
        required=True,
        ondelete="cascade",
    )
    image = fields.Binary(string="Image")
    name = fields.Char(string="Image name")
