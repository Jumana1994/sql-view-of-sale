# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderDetails(models.Model):
    _name = "sale.order.details"
    _description = "Sale Order Details"
    _auto = False

    name = fields.Char(string="Reference")
    company_id = fields.Many2one('res.company',string="Company")
    partner_id = fields.Many2one('res.partner',string="partner")
    date_order = fields.Datetime(string="Order date")
    # amount_total = fields.Monetary(string="Total", store=True)

    def init(self):
        self._cr.execute(""" 
           CREATE OR REPLACE VIEW sale_order_details AS ( 
               SELECT            row_number() OVER () as id,
                ps.company_id as company_id,  
                ps.name as name,
                ps.partner_id as partner_id,
                ps.date_order as date_order
                FROM sale_order ps 
                INNER JOIN  res_partner ON ps.partner_id = res_partner.id
                INNER JOIN  res_company ON ps.company_id = res_company.id)
    """)


