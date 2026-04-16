from odoo import models, fields

class HelpdeskTicketStage(models.Model):
    _name = 'helpdesk.ticket.stage'
    _description = 'Ticket Stage'
    _order = 'sequence'

    name = fields.Char(string='Stage Name', required=True)
    sequence = fields.Integer(default=10)
    is_done_stage = fields.Boolean(string='Is Done Stage', help='Triggers Approval')
    is_cancelled_stage = fields.Boolean(string='Is Cancelled Stage')
    fold = fields.Boolean(string='Folded in Kanban')
    description = fields.Text(string='Description')