# Copyright (c) 2024, lakshman and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	#columns, data = [], []
	return get_columns(), get_data()

def get_data():

    query = """ 
        SELECT 
            sq_sub.name AS quotation_name,
            sq_sub.supplier,
            sq_sub.transaction_date AS quotation_transaction_date,
            sq_sub.opportunity AS quotation_opportunity,
            sq_sub.item_name AS quotation_item_name,
            sq_sub.qty AS quotation_item_qty,
            sq_sub.rate AS quotation_item_rate,
            sq_sub.amount AS quotation_item_amount
        FROM (
            SELECT
                sq.name,
                sq.supplier,
                sq.transaction_date,
                sq.opportunity,
                it.item_name,
                it.qty,
                it.rate,
                it.amount
            FROM
                `tabSupplier Quotation` AS sq
            LEFT JOIN
                `tabSupplier Quotation Item` AS it ON sq.name = it.parent
        ) AS sq_sub     
        
        ORDER BY sq_sub.name,sq_sub.item_name ASC;
    """
    data = frappe.db.sql(query)
    return data

def get_columns():
    return [
        "Suppler Quotation id:Data:200",
        "Supplier:Link/supplier:200",
        "Transaction Date:Date:100",
        "Opportunity:Link/Opportunity:200",
        "Item name:Data:200",
        "qty:Float:100",
        "Rate:Float:100",
        "item amount:Currency:100"
           
    ]



# select  sq.name,sq.supplier,sq.transaction_date,sq.opportunity,it.item_name,it.qty,it.rate,it.amount 
# from `tabSupplier Quotation`as sq
# left join `tabSupplier Quotation Item` AS it On opp.name=sq.parent