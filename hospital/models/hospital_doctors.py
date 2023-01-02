# -*- coding: utf-8 -*-

from odoo import models, fields

class HospitalModel(models.Model):
    _name = "hospital.doctors"
    _description = "Hospital Doctors Model"

    name = fields.Char('Name', required=True)
    qualification = fields.Char('Qualification')
    gender = fields.Selection(
        string="Gender",
        selection=[('male', 'Male'), ('female', 'Female')]
    )
    dob = fields.Date('Date Of Birth')
    age = fields.Integer('Age')
    phone_number = fields.Char('Phone Number', required=True)
    email = fields.Char('E-mail')
    availability = fields.Boolean()
    specialization = fields.Char('Specialist Of', required=True)
    fees = fields.Integer('Fees', required=True)
    rating = fields.Selection(
        string="Ratings",
        selection=[('one', '*'), ('two', '**'), ('three', '***'), ('four', '****'), ('five', '*****')]
    )
    