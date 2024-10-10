# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Easy Attribute Columns",
    'version': '0.1.0.1',
    'author': "Fondamental Group - Arnaud Gay",
    'description': """
    Add the fields
        -attribute1 (txt)
        -attribute2 (txt)
        -attribute3 (txt)
        -attribute4 (txt)
        in product.product. with the attribute text value
        add cron fucntion for updates datas:
        model._cron_compute_attribute_variants()
""",
    'website': 'https://www.fondamental-corporate.com/',
    'depends': ['stock'],
    'data': [
             ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
