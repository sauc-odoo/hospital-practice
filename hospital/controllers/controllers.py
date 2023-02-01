# -*- coding: utf-8 -*-
from odoo import http

class Hospital(http.Controller):

    @http.route('/hospital/hospital/', auth='public', website=True)
    def index(self, **kw):
        Patients = http.request.env['hospital.patients']
        return http.request.render('hospital.index', {'patients': Patients.search([])})

    @http.route('/hospital/<model("hospital.patients"):patient>/', auth='public', website=True)
    def patient(self, patient):
        return http.request.render('hospital.listing', {'person': patient})
