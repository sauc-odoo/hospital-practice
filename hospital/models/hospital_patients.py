# -*- coding: utf-8 -*-

from odoo import models, fields

class HospitalModel(models.Model):
    _name = "hospital.patients"
    _description = "Hospital Patients Model"

    name = fields.Char('Name', required=True)
    gender = fields.Selection(
        string="Gender",
        selection=[('male', 'Male'), ('female', 'Female')]
    )
    dob = fields.Date('Date Of Birth')
    age = fields.Integer('Age', required=True)
    height = fields.Char('Height')
    weight = fields.Char('Weight')
    diagnosis = fields.Char('Diagnosis', required=True, default="Regular Checkup")
    prescription = fields.Text()
    temperature = fields.Char('Temperature')
    blood_pressure = fields.Char('Blood Pressure')
    sugar_level = fields.Char('Sugar Level')
    phone_number = fields.Char('Phone Number')
    