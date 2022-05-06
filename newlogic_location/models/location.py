# -*- coding: utf-8 -*-

from odoo import fields, models

class G2PLocation(models.Model):
    _name = 'g2p.location'
    _description = 'Location'
    _order = 'id desc'

    name = fields.Char('Name')
    code = fields.Char('Code')
    altnames = fields.Char('Alternate Name')
    level = fields.Integer('Level')

