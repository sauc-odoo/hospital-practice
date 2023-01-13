# -*- coding: utf-8 -*-

from odoo import models, fields

class HospitalModel(models.Model):
    _name = "hospital.general.problems"
    _description = "Hospital Category - General Problems Model"
    _order = "name"

    name = fields.Char('Name')
    list_general_problems_patients = fields.One2many('hospital.patients', 'general_problems_id', string="List of patients")
    