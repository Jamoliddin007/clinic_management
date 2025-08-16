from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ClinicPrescription(models.Model):
    _name = 'clinic.prescription'
    _description = 'Prescription'
    _order = 'date desc'

    appointment_id = fields.Many2one('clinic.appointment', string="Appointment", required=True, ondelete='cascade')
    doctor_id = fields.Many2one('clinic.doctor', string="Doctor", required=True)
    date = fields.Date("Date", default=fields.Date.context_today, required=True)
    instructions = fields.Text("General Instructions")
    line_ids = fields.One2many('clinic.prescription.line', 'prescription_id', string="Lines")

    _sql_constraints = [
        ('uniq_appointment_one_rx', 'unique(appointment_id)', 'Only one prescription per appointment is allowed.')
    ]

    @api.onchange('appointment_id')
    def _onchange_appointment(self):
        if self.appointment_id:
            self.doctor_id = self.appointment_id.doctor_id.id
