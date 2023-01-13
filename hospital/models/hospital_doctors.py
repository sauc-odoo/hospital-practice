# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class HospitalModel(models.Model):
    _name = "hospital.doctors"
    _description = "Hospital menu - Doctors Model"
    _order = "id desc"

    name = fields.Char('Name', required=True)
    qualification = fields.Char('Qualification')
    gender = fields.Selection(
        string="Gender",
        selection=[('male', 'Male'), ('female', 'Female')]
    )
    dob = fields.Date('Date Of Birth')
    doctor_age = fields.Integer('Age', compute="_compute_doctor_age", store=True)
    date = fields.Date(readonly = True, default= lambda self: fields.datetime.now())
    phone_number = fields.Char('Phone Number', required=True)
    email = fields.Char('E-mail')
    availability = fields.Boolean()
    specialization = fields.Char('Specialist Of')
    fees = fields.Float('Fees', required=True)
    success_rate = fields.Integer('Success Rate')

    _sql_constraints = [
        ('check_success_rate', 'CHECK(success_rate <= 100 AND success_rate >= 0)',
         'The Success rate should be appropriate')
    ]

    @api.depends("dob", "date")
    def _compute_doctor_age(self):
        for record in self:
            record.doctor_age = relativedelta(record.date, record.dob).years

    def action_autofill(self):
        for record in self:
            record.qualification = "MBBS"
            record.gender = 'male'
            record.dob = "1990-01-01"
            record.doctor_age = 30
            record.email = "demodoctor@example.com"
            record.availability = True
            record.specialization = "Medicine"
            record.success_rate = 90

    @api.constrains('phone_number')
    def _check_phone_number(self):
        for record in self:
            for i in record.phone_number:
                if ord(i) < 48 or ord(i) > 57:
                    raise ValidationError("enter digits")
            if len(record.phone_number) != 10:
                raise ValidationError("phone number should be of 10 digits")
    