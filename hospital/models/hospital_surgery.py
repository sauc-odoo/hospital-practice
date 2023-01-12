# -*- coding: utf-8 -*-

from odoo import models, fields

class HospitalModel(models.Model):
    _name = "hospital.surgery"
    _description = "Hospital Category - Surgery Model"

    name = fields.Char('Name')
    list_surgery_patients = fields.One2many('hospital.patients', 'surgery_id', string="List of patients")
    