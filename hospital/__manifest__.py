# -*- coding: utf-8 -*-

{
    'name' : "Hospital Module",
    'version' : '1.0',
    'author' : "Saurabh Choraria",
    'description' : "It is a module for hospital management",
    'depends' : ['mail'],
    'data' : [
            'security/ir.model.access.csv',
            
            'views/hospital_patients_views.xml',
            'views/hospital_doctors_views.xml',
            'views/hospital_category_views.xml',
            'views/hospital_bed_type_views.xml',
            'views/hospital_bills_views.xml',
            'views/hospital_views_action.xml',
        ],
    'demo' : [
            'demo/hospital_patients_demo.xml',
        ],    
    'application' : True,
}