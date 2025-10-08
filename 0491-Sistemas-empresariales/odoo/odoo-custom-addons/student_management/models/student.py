from odoo import models, fields

class Student(models.Model):
    _name = 'student.management'
    _description = 'Student'

    student_id = fields.Char(string='Student ID', required=True)
    name = fields.Char(string='Student Name', required=True)
    age = fields.Integer(string='Student Age')
    date_of_birth = fields.Date(string='Date of Birth')
