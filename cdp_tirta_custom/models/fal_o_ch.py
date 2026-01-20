from odoo import fields, models, api, _
from odoo.exceptions import UserError
import base64
import datetime
from openpyxl import load_workbook
from io import BytesIO
from odoo.exceptions import UserError


class FalOCh(models.Model):
    _inherit = 'fal.o.ch'


    def create(self, vals_list):
        result = super(FalOCh,self).create(vals_list)
        for rec in result:
            if rec.channel_type == 'lazada':
                rec.name = self.env['ir.sequence'].next_by_code('fal.o.ch.lazada') or '/'
        return result   