from odoo import models, fields

class ClinicPrescriptionLine(models.Model):
    _name = 'clinic.prescription.line'
    _description = 'Prescription Line'

    prescription_id = fields.Many2one('clinic.prescription', string="Prescription", required=True, ondelete='cascade')
    medicine_id = fields.Char(string="Medicine")
    dosage = fields.Char("Dosage")
    frequency = fields.Char("Frequency")
    duration = fields.Char("Duration")
    note = fields.Text("Note")
