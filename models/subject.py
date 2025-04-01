# -*- coding: utf-8 -*-
from odoo import models, fields, api

class EducationSubject(models.Model):
    _name = 'education.subject'
    _description = 'Education Subject'

    name = fields.Char('Name')
    description = fields.Text('Description') 
    unit_credit = fields.Integer('Unit Credit')
    teacher_id = fields.Many2one('education.teacher', string='Assigned Teacher')