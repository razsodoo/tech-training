import re  # Required for pattern matching
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = "registry_number"

    certificate_title = fields.Binary()
    current_mileage = fields.Float()
    date_registry = fields.Date()
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    license_plate = fields.Char(required=True)
    registry_number = fields.Char(required=True, copy=False, readonly=True, default="MRN0000")
    vin = fields.Char(required=True, copy=False, )

    _sql_constraints = [
        ('registry_number_unique', 'unique(registry_number)', 'The registry number must be unique.'),
        ('license_plate_unique', 'unique(license_plate)', 'The licence plate must be unique.'),
        ('vin_unique', 'unique(vin)', 'The VIN must be unique.'),
    ]

    # Override create method to assign sequential registry_number
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ("MRN0000")) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('motorcycle.registry') or 'MRN0000'
        return super().create(vals_list)

    # Validate patterns
    @api.constrains('vin', 'license_plate')
    def _check_vin_and_license_plate_format(self):
        vin_pattern = r'^[A-Z]{2}\d{2}[A-Z0-9]{2}\d{5}$'
        plate_pattern = r'^[A-Z]{1,4}\d{1,3}[A-Z]{0,2}$'
        for rec in self:
            if rec.vin and not re.match(vin_pattern, rec.vin):
                raise ValidationError("Invalid VIN format. Example: KAIN220M00234")
            if rec.license_plate and not re.match(plate_pattern, rec.license_plate):
                raise ValidationError("Invalid License Plate format. Example: KLV453 or KLR3453L")
