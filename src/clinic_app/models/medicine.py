from odoo import models, fields

class ClinicMedicine(models.Model):
    _name = 'clinic.medicine'
    _description = 'Medicine'
    _order = 'name'

    name = fields.Char("Name", required=True)
    generic_name = fields.Char("Generic Name")
    dosage_unit = fields.Char("Dosage Unit")  # mg/ml/tablet
    description = fields.Text("Description")
    manufacturer = fields.Char("Manufacturer")
    contraindications_text = fields.Text("Contraindications")

    contraindicated_ids = fields.Many2many(
        'clinic.medicine', 'medicine_contra_rel',
        'medicine_id', 'contra_medicine_id',
        string="Contraindicated with"
    )
