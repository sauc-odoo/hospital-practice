# -*- coding: utf-8 -*-

from odoo import models, fields

class HospitalModel(models.Model):
    _name = "hospital.testing"
    _description = "Hospital Category - Testing Model"
    _order = "name"

    name = fields.Char('Name')
    color = fields.Integer()
    list_testing_patients = fields.One2many('hospital.patients', 'testing_ids')
    