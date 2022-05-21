#
# Copyright (c) 2022 Newlogic.
#
# This file is part of newlogic-g2p-erp.
# See https://github.com/newlogic/newlogic-g2p-erp/ for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import json

from odoo.addons.component.core import Component

import logging
_logger = logging.getLogger(__name__)

class G2PResPartnerGroupDataRecordImporter(Component):
    _name = "g2p.res.partner.group.data.importer"
    _inherit = ["importer.record"]
    _apply_on = "res.partner"
    odoo_unique_key = "id"
    odoo_unique_key_is_xmlid = True

    def prepare_line(self, line):
        res = super().prepare_line(line)
        odk_id = res["__id"].split(":")[1]
       
        new_res = {
            "id": f"odk.group.{odk_id}",
            "name": res['registration_mrz']['document_number'],
            "registration_date": '2000-01-25',
            "is_registrant": 'True',
            "is_group": 'True',
            "_line_nr": -1,
        }
        _logger.debug(f"Result: {new_res}")
        return new_res
