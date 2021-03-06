# -*- coding: utf-8 -*-
{
    'name': "DLS_Projects",

    'summary': """Manage trainings""",

    'description': """
        PRO projects system:
            - create projects
            - create jobs
            - create employees
            - create teems
            - create invoices
    """,

    'author': "Danielius Štuikys",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}