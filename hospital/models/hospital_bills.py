# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HospitalModel(models.Model):
    _name = "hospital.bills"
    _description = "Hospital menu - Bills"

    bill_number = fields.Integer('Bill Number')
    patient_id = fields.Many2one('hospital.patients', string="Patient's Name")
    doctor_id = fields.Many2one('hospital.doctors', string="Doctor's Name")
    fees = fields.Float(string="Doctor's Fees", related="doctor_id.fees")
    bed_type_id = fields.Many2one('hospital.bed.type', string="Bed Type")
    no_of_days = fields.Integer('No. of Days in Bed')
    bed_price = fields.Float(string="Bed Price", related="bed_type_id.price")
    total_bed_price = fields.Float(string="Total Bed Price", compute="_compute_total_bed_price")
    total_bill = fields.Float(string="Total Bill Price", compute="_compute_total_bill")
    status = fields.Selection(
        selection=[('paid', 'Paid'), ('due', 'Due'),], default='due'
    )

    @api.depends("no_of_days", "bed_price")
    def _compute_total_bed_price(self):
        for record in self:
            record.total_bed_price = record.no_of_days * record.bed_price

    @api.depends("fees", "total_bed_price")
    def _compute_total_bill(self):
        for record in self:
            record.total_bill = record.fees + record.total_bed_price

    def action_paid(self):
        for record in self:
            record.status = "paid"
        self.patient_id.state = "billing"

    def action_due(self):
        for record in self:
            record.status = "due"
        self.patient_id.state = "billing"