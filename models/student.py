# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta

class EducationStudent(models.Model):
    _name = 'education.student'
    _description = 'Education Student'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(
        'res.partner',
        string='Related Partner',
        required=True,
        ondelete='cascade'
    )
    birthdate = fields.Date(
        string='Birthdate'
    )
    age = fields.Integer(
        string='Age',
        compute='_compute_age',
        store=True
    )

    @api.depends('birthdate')
    def _compute_age(self):
        """Compute student age based on birthdate"""
        for record in self:
            if not record.birthdate:
                continue
            
            record.age = relativedelta(date.today(), record.birthdate).years