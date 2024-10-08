from odoo import fields, models, api
import logging
_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
    _inherit = "product.product"
    product_template_variant_value_ids = fields.Many2many('product.template.attribute.value',
                                                          relation='product_variant_combination',
                                                          domain=[('attribute_line_id.value_count', '>', 0)],
                                                          string="Variant Values", ondelete='restrict')

    fg_attribute1 = fields.Text("Attribute 1")
    fg_attribute2 = fields.Text("Attribute 2")
    fg_attribute3 = fields.Text("Attribute 3")
    fg_attribute4 = fields.Text("Attribute 4")

    @api.depends('product_template_attribute_value_ids')
    def _compute_combination_indices(self):
        for product in self:
            product.combination_indices = product.product_template_attribute_value_ids._ids2str()
            i = 1
            for fg_values in product.product_template_attribute_value_ids:
                if i == 1:
                    product.fg_attribute1 = fg_values.product_attribute_value_id.name
                elif i == 2 :
                    product.fg_attribute2 = fg_values.product_attribute_value_id.name
                elif i == 3 :
                    product.fg_attribute3 = fg_values.product_attribute_value_id.name
                elif i == 4:
                    product.fg_attribute4 = fg_values.product_attribute_value_id.name
                i += 1

    def _cron_compute_attribute_variants(self):
        for product in self.env["product.product"].search([]):
            if product.product_template_attribute_value_ids:
                i = 1
                for fg_values in product.product_template_attribute_value_ids:
                    if i == 1:
                        product.fg_attribute1 = fg_values.product_attribute_value_id.name
                    elif i == 2:
                        product.fg_attribute2 = fg_values.product_attribute_value_id.name
                    elif i == 3:
                        product.fg_attribute3 = fg_values.product_attribute_value_id.name
                    elif i == 4:
                        product.fg_attribute4 = fg_values.product_attribute_value_id.name
                    i += 1



