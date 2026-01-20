from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = "res.partner"
    
    x_granted_users_ids = fields.Many2many(
        "res.partner",
        "fal_account_invoice_send_wizard_res_partner_rel",
        "wizard_id",
        "partner_id",
        "Followers",
    )