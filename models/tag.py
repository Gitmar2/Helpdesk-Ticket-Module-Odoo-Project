from odoo import models, fields

class HelpdeskTag(models.Model):
    _name = 'helpdesk.tag'
    _description = 'Ticket Tag'

    name = fields.Char(required=True)
    color = fields.Integer()
