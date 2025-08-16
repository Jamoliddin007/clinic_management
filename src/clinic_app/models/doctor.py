from odoo import models, fields

class Doctor(models.Model):
    _name = 'clinic.doctor'
    _description = 'Doctor'

    name = fields.Char(string="Name", required=True)
    specialty = fields.Char(string="Specialty")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
