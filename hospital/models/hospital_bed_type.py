# -*- coding: utf-8 -*-

from odoo import models, fields

class HospitalModel(models.Model):
    _name = "hospital.bed.type"
    _description = "Hospital Bed allocation - bed type Model"

    name = fields.Char('Type', required=True)
    price = fields.Float('Price', required=True)
    image = fields.Binary()

    _sql_constraints = [
        ('check_name', 'unique(name)',
         'The type of bed should be unique')
    ]