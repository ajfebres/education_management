# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class EducationEnrollment(models.Model):
    _name = 'education.enrollment'
    _description = 'Course Enrollment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date desc'

    name = fields.Char(
        string='Reference',
        readonly=True,
        default=_('New')
    )
    student_id = fields.Many2one(
        'education.student',
        string='Student',
        required=True
    )
    course_id = fields.Many2one(
        'education.course',
        string='Course',
        required=True
    )
    date = fields.Date(
        string='Enrollment Date',
        default=fields.Date.context_today
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed')
    ], string='Status',
        default='draft'
    )

    @api.model
    def create(self, vals):
        """Generate sequence for enrollment reference"""
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('education.enrollment')
        return super().create(vals)

    def action_pending(self):
        """Confirm enrollment"""
        self.write({'state': 'pending'}) 

    def action_cancel(self):
        """Cancel enrollment"""
        self.write({'state': 'canceled'})

    def action_complete(self):
        """Mark enrollment as completed"""
        self.write({'state': 'completed'})