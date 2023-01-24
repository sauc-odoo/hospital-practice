# -*- coding: utf-8 -*-

from odoo import models, fields, Command

class HospitalAccount(models.Model):
    _inherit = "hospital.patients"

    def action_treated(self):
        
        self.env["account.move"].create(
            {
                'partner_id': self.bill_initiator.id,
                'move_type': 'out_invoice',
                'invoice_line_ids': [
                Command.create(
                    {
                        "name": self.name,
                        "quantity": 1,
                        "price_unit": self.amount_paid,
                    }),
                Command.create(
                    {
                        "name": "Nurse fees",
                        "quantity": 1,
                        "price_unit": 100.00,
                    }
                )
            ],
            }
        )
        return super(HospitalAccount,self).action_treated()