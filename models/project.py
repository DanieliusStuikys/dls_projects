from odoo import models, fields, api

class Projektai(models.Model):
    _name = 'pro_projects.project'
    _descriptioni = "Projects"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description  ")
    start_date = fields.Date(string="Start Date")
    start_end = fields.Date(string="End Date")
