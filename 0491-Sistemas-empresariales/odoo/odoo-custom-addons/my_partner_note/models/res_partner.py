from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    x_note = fields.Char(string="Custom Note")  # single custom field
