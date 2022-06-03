# Part of Newlogic G2P. See LICENSE file for full copyright and licensing details.
from odoo import api, models


class POSCategory(models.Model):
    _inherit = "pos.category"

    @api.model
    def get_voucher_categ(self):
        data = self.env["ir.model.data"].search(
            [("name", "=", "voucher_product_categ_pos"), ("model", "=", "pos.category")]
        )
        if data:
            return data[0].res_id
