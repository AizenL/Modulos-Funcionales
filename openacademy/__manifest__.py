# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Modulo creado para la base de un modulo""",

    'description': """
        El proposito de este modulo es crear un modulo funcional
    """,

    'author': "OGGonzalezM",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'views/openacademy_course_view.xml',
        'views/openacademy_session_view.xml',
        'views/partner_view.xml',
        'workflow/openacademy_session_workflow.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/openacademy_wizard_view.xml',
        'report/openacademy_session_report.xml',
        'views/openacademy_session_board_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
