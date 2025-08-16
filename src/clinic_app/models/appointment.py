from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Appointment(models.Model):
    _name = 'clinic.appointment'
    _description = 'Appointment'
    _order = 'start_time desc'

    patient_id = fields.Many2one('clinic.patient', string="Patient", required=True)
    doctor_id = fields.Many2one('clinic.doctor', string="Doctor", required=True)
    start_time = fields.Datetime(string="Start", required=True)
    end_time = fields.Datetime(string="End", required=True)
    status = fields.Selection([
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('done', 'Done'),
    ], default='new', required=True)
    urgency = fields.Selection([
        ('normal', 'Normal'),
        ('urgent', 'Urgent'),
    ], default='normal')
    short_diagnosis = fields.Char(string="Diagnosis (short)")

    @api.constrains('start_time', 'end_time', 'doctor_id', 'status')
    def _check_overlap(self):
        for rec in self:
            if not rec.start_time or not rec.end_time or not rec.doctor_id:
                continue
            if rec.end_time <= rec.start_time:
                raise ValidationError("End must be after Start.")
            domain = [
                ('id', '!=', rec.id),
                ('doctor_id', '=', rec.doctor_id.id),
                ('status', 'in', ['new', 'confirmed']),
                ('start_time', '<', rec.end_time),
                ('end_time', '>', rec.start_time),
            ]
            if self.search_count(domain):
                raise ValidationError("Doctor already has an appointment in this time range.")
