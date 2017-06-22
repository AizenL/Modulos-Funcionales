# -*- coding: utf-8 -*-
{
    'name': "Merced",

    'summary': """
        Agregar campo a res.partner""",

    'description': """
        Adding field to res.partner
    """,

    'author': "OGGonzalezM",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        'views/add_field_view.xml',
        'views/generador_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}