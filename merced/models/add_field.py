# -*- coding: utf-8 -*-

from odoo import models, fields

class Add_field(models.Model):
	_inherit = 'res.partner'

	x_identificador = fields.Char(string=" Identificador ")
