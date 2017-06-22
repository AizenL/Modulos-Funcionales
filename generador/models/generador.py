# -*- coding: utf-8 -*-
from odoo import api, models, fields

class Generador1(models.Model):
    # Revisar la forma de herencia
    
    _inherit = 'product.template'
    
    #General codigo de barras
    @api.multi
    def gen_codigos(self):
        nom_proveedor = self.seller_ids
        
        prov = str(nom_proveedor)
        print "**************" + str(nom_proveedor) + "***********************"
        if not nom_proveedor :
            return {
                'warning': {
                    'title': "Incorrecto, no hay proveedor",
                    'message': "Por favor elija un proveedor en la pestania de inventario",
                },
            }
        else:
            prefijo = nom_proveedor[0]
            numero = 1000000000 + self.id
            num_str = str(numero)
            #codigo = prefijo + str(num_str[1:10])
            self.barcode = prefijo + str(num_str[1:10])
            #return super(self, barcode).write(barcode=barcode)


#def write(self, cr, uid, vals, context=None):
#       name = str(vals['first_name'] or '') + ' ' +str(vals['last_name'] or '')
#       vals['name'] = name
#       return super(hr_employee, self).write(cr, uid, vals, context=context)