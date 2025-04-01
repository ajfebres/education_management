# -*- coding: utf-8 -*-
{
    'name': 'Education Management',
    'version': '1.0.1',
    'summary': 'Manage students, courses, subjects, and teachers',
    'description': """
        Educational module for handling enrollments, courses, subjects, and teachers.
    """,
    'author': 'Abraham J. Febres',
    'category': 'Education',
    'depends': [
        'base', 
        'product'
    ],
    'data': [
        'data/sequence_data.xml',
        'security/groups_views.xml',
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/teacher_views.xml',
        'views/subject_views.xml',
        'views/course_views.xml',
        'views/enrollment_views.xml',
        'views/menuitem_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}