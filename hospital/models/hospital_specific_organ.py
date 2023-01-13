# -*- coding: utf-8 -*-

from odoo import models, fields

class HospitalModel(models.Model):
    _name = "hospital.specific.organ"
    _description = "Hospital Category - Specific Organ Model"
    _order = "sequence, name"

    name = fields.Char('Name')
    list_specific_organ_patients = fields.One2many('hospital.patients', 'specific_organ_id', string="List of patients")
    sequence = fields.Integer('Sequence', default=1)
    