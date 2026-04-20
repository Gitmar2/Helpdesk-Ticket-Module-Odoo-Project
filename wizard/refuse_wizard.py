from odoo import models, fields, api

class HelpdeskRefuseWizard(models.TransientModel):
    _name = 'helpdesk.refuse.wizard'
    _description = 'Refuse Reason Wizard'

    ticket_id = fields.Many2one('helpdesk.ticket', string='Ticket', required=True)
    refused_reason = fields.Text(string='Refuse Reason', required=True)

    def action_confirm(self):
        self.ensure_one()
        self.ticket_id.write({
            'refused_reason': self.refused_reason,
            'state': 'refused',
        })
        self.ticket_id.message_post(
            body=f'Ticket refused. Reason: {self.refused_reason}'
        )
        return {'type': 'ir.actions.act_window_close'}