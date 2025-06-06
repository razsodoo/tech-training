import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = "registry_number"

    certificate_title = fields.Binary()
    current_mileage = fields.Float()
    date_registry = fields.Date()
    license_plate = fields.Char(required=True)
    registry_number = fields.Char(required=True, copy=False, readonly=True, default="MRN0000")
    vin = fields.Char(required=True, copy=False)

    # New fields
    owner_id = fields.Many2one('res.partner', string="Owner")
    email = fields.Char(related='owner_id.email', readonly=True)
    phone = fields.Char(related='owner_id.phone', readonly=True)

    make = fields.Char(compute='_compute_vin_fields', store=True)
    model = fields.Char(compute='_compute_vin_fields', store=True)
    year = fields.Char(compute='_compute_vin_fields', store=True)

    _sql_constraints = [
        ('registry_number_unique', 'unique(registry_number)', 'The registry number must be unique.'),
        ('license_plate_unique', 'unique(license_plate)', 'The licence plate must be unique.'),
        ('vin_unique', 'unique(vin)', 'The VIN must be unique.'),
    ]
                    
    @api.depends('vin')
    def _compute_vin_fields(self):
        for rec in self:
            if rec.vin and len(rec.vin) >= 6:
                rec.make = rec.vin[:2]
                rec.model = rec.vin[2:4]
                rec.year = rec.vin[4:6]
            else:
                rec.make = rec.model = rec.year = False

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ("MRN0000")) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('motorcycle.registry') or 'MRN0000'
        return super().create(vals_list)

    @api.constrains('vin', 'license_plate')
    def _check_vin_and_license_plate_format(self):
        vin_pattern = r'^[A-Z]{2}\d{2}[A-Z0-9]{2}\d{5}$'
        plate_pattern = r'^[A-Z]{1,4}\d{1,3}[A-Z]{0,2}$'
        for rec in self:
            if rec.vin and not re.match(vin_pattern, rec.vin):
                raise ValidationError("Invalid VIN format. Example: KAIN220M00234")
            if rec.license_plate and not re.match(plate_pattern, rec.license_plate):
                raise ValidationError("Invalid License Plate format. Example: KLV453 or KLR3453L")
