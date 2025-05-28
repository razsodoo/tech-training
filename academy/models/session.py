from odoo import fields, models

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Course Session'

    name = fields.Char(string="Session Title", required=True)
    start_date = fields.Date(string="Start Date")
    duration = fields.Float(string="Duration (days)")
    course_id = fields.Many2one('academy.course', string="Course", required=True)