# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class EducationCourse(models.Model):
    _name = 'education.course'
    _description = 'Education Course'
    _inherits = {'product.template': 'product_tmpl_id'}
    
    product_tmpl_id = fields.Many2one(
        'product.template',
        string='Related Product',
        required=True,
        ondelete='cascade'
    )
    
    teacher_ids = fields.Many2many(
        'education.teacher',
        string='Teachers',
        compute='_compute_teacher_by_subject',
        store=True
    )
    subject_ids = fields.Many2many(
        'education.subject',
        string='Subjects'
    )
    start_date = fields.Date(
        string='Start Date'
    )
    duration = fields.Integer(
        string='Duration (weeks)'
    )
    max_capacity = fields.Integer(
        string='Maximum Capacity'
    )
    remaining_capacity = fields.Integer(
        string='Remaining Seats',
        compute='_compute_remaining_capacity'
    )
    enrollment_ids = fields.One2many(
        'education.enrollment',
        'course_id',
        string='Enrollments'
    )

    @api.depends('max_capacity', 'enrollment_ids')
    def _compute_remaining_capacity(self):
        """Calculate remaining capacity in course"""
        for course in self:
            completed_enrollments = course.enrollment_ids.filtered(
                lambda e: e.state == 'completed'
            )
            course.remaining_capacity = course.max_capacity - len(completed_enrollments)

    @api.depends("subject_ids")
    def _compute_teacher_by_subject(self):
        for record in self:
            if not record.subject_ids:
                continue
            record.teacher_ids = record.subject_ids.mapped("teacher_id").ids