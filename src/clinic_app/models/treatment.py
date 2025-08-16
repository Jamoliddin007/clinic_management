from odoo import models, fields

class Treatment(models.Model):
    _name = "clinic.treatment"
    _description = "Treatment"

    name = fields.Char(string="Treatment Name", required=True)
    description = fields.Text(string="Description")
    diagnosis_id = fields.Many2one("clinic.diagnosis", string="Diagnosis", required=True)
    doctor_id = fields.Many2one("clinic.doctor", string="Doctor", required=True)
    patient_id = fields.Many2one("clinic.patient", string="Patient", required=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    status = fields.Selection([
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled")
    ], string="Status", default="ongoing")
