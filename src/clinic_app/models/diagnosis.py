from odoo import models, fields

class Diagnosis(models.Model):
    _name = 'clinic.diagnosis'
    _description = 'Diagnosis'

    patient_id = fields.Many2one('clinic.patient', string="Patient", required=True)
    doctor_id = fields.Many2one('clinic.doctor', string="Doctor", required=True)
    diagnosis = fields.Text(string="Diagnosis", required=True)
    date = fields.Datetime(string="Date", required=True, default=fields.Datetime.now)
