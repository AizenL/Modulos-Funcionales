# -*- coding: utf-8 -*-
{
    'name': "Generador CB",

    'summary': """
        Generador de codigos""",

    'description': """
        Este modulo genera codigos de identificacion para los productos registrados de acuerdo a su proveedor
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        'views/generador_view.xml',
        'views/letra_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
