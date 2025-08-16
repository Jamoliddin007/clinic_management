from odoo import models, fields

class Patient(models.Model):
    _name = "clinic.patient"
    _description = "Patient"

    name = fields.Char(string="Full Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
