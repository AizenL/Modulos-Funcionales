from odoo import api, models, fields

class Letra(models.Model):

	_inherit = 'product.supplierinfo'
	letter_pro = fields.Char(string="Letra")
