# -*- coding: utf-8 -*-
from odoo import models, fields, api

class EducationTeacher(models.Model):
    _name = 'education.teacher'
    _description = 'Education Teacher'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(
        'res.partner',
        string='Related Partner',
        required=True,
        ondelete='cascade'
    )
    subject_ids = fields.One2many(
        'education.subject',
        'teacher_id',
        string='Subjects',
        readonly=True
    )