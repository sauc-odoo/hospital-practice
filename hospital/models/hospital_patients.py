# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class HospitalModel(models.Model):
    _name = "hospital.patients"
    _description = "Hospital Patients Model"

    name = fields.Char('Name', required=True)
    gender = fields.Selection(
        string="Gender",
        required=True,
        selection=[('male', 'Male'), ('female', 'Female')]
    )
    dob = fields.Date('Date Of Birth')
    date = fields.Date(readonly = True, default= lambda self: fields.datetime.now())
    age = fields.Integer('Age', compute="_compute_age")
    height = fields.Float('Height')
    weight = fields.Float('Weight')
    diagnosis = fields.Char('Diagnosis', required=True, default="Regular Checkup")
    prescription = fields.Text()
    temperature = fields.Char('Temperature')
    blood_pressure = fields.Char('Blood Pressure')
    sugar_level = fields.Char('Sugar Level')
    phone_number = fields.Char('Phone Number')
    testing_ids = fields.Many2many('hospital.testing', string="Testings")
    specific_organ_id = fields.Many2one('hospital.specific.organ', string="Organ effected")
    surgery_id = fields.Many2one('hospital.surgery', string="Surgery")
    general_problems_id = fields.Many2one('hospital.general.problems', string="General Problems")

    _sql_constraints = [
        ('check_height', 'CHECK(height >= 0)',
         'The height should be positive'),
        ('check_weight', 'CHECK(weight >= 0)',
         'The weight should be positive')
    ]

    @api.depends("dob", "date")
    def _compute_age(self):
        for record in self:
            record.age = relativedelta(record.date, record.dob).years

    @api.constrains('phone_number')
    def _check_phone_number(self):
        for record in self:
            for i in record.phone_number:
                if ord(i) < 48 or ord(i) > 57:
                    raise ValidationError("enter digits")
            if len(record.phone_number) != 10:
                raise ValidationError("phone number should be of 10 digits")