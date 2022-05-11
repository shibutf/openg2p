# -*- coding: utf-8 -*-
#################################################################################
#   Copyright 2022 Newlogic
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#################################################################################
from odoo import _, api, fields, models
from uuid import uuid4

class G2PProgram(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = "g2p.program"
    _description = "Program"
    _order = 'id desc'
    _check_company_auto = True

    name = fields.Char(required=True, tracking=True)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company, tracking=True)
    target_type = fields.Selection(
        selection=[('group', 'Group'), ('individual', 'Individual')],
        default='group')

    enrollement_criterias = fields.Selection(
        [])
    entitlement_calculation = fields.Selection(
        [])
    cycle_creator = fields.Selection(
        [])
    end_of_program = fields.Selection([]) # Hook for end of program

    number_of_cycles = fields.Integer(default=1)

    program_membership_ids = fields.One2many('g2p.program_membership','program_id','Program Memberships')
    cycle_ids = fields.One2many('g2p.cycle','program_id','Cycles')

    # Group able to validate the payment
    # Todo: Create a record rule for payment_validation_group
    payment_validation_group_id = fields.Many2one('res.groups', string='Payment Validation Group')

