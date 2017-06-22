# -*- coding: utf-8 -*-

from odoo import fields, models


class Partner(models.Model):

    _inherit = 'res.partner'
    # Herencia Odoo

    instructor = fields.Boolean(default=False)
    session_ids = fields.Many2many('openacademy.session', string="Session as attendee", readonly=True)
