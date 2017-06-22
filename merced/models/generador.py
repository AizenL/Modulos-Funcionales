from odoo import api, exceptions, fields, models

class Generador(models.Model):
	_inherit = 'product.template'

	msj_error = fields.Text(string="Error de proveedor", default="Por favor agregue un proveedor", readonly=True, store=False)

	@api.multi
	def imprimir(self):
		try:
			prov_id = self.seller_ids[0].name
			#( name= id proveedor)
			ident_prov = prov_id.x_identificador
			print "***********************" +  str(ident_prov) + " ***********************"
			if ident_prov == False:
				print "*** No hay proveedor"
				#self.barcode = None
				self.write({'barcode': ''})
				self.write({'msj_error': 'Por favor agregue un proveedor'})
			else:
				numero = 1000000000 + self.id
				print " * *** * " + str(numero) + " * *** * "
				num_str = str(numero)
				cod_barras = str(ident_prov) + str(num_str[1:10])
				#self.barcode = cod_barras
				self.write({'barcode': cod_barras})
				self.write({'msj_error': 'Por favor agregue un proveedor'})
		except IndexError as e:
			self.write({'barcode': ' '})
			self.write({'msj_error': 'Por favor agregue un proveedor'})
