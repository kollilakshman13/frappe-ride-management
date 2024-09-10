# Copyright (c) 2024, lakshman and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	#columns, data = [], []
	return get_columns(), get_data()
def get_data():
    query = """
        SELECT 
            c.name AS c_name,
            ci.item_name AS ci_item_name,
            ci.item_code AS ci_item_code,
            ci.qty AS ci_qty,
            ci.rate AS ci_rate,
            ci.amount AS ci_amount,
            ci.supplier AS ci_supplier,
            ci.supplier_item as ci_supplier_item,
            ci.supplier_rate as ci_supplier_rate,
            ci.supplier_amount AS ci_supplier_amount,
            ci.amount - ci.supplier_amount AS difference_amount,
            cis.sales_person AS cis_sales_person

        FROM 
            `tabCustomer Order Form` as c 
        LEFT JOIN `tabCustomer Order Item` as ci on c.name= ci.parent
        LEFT JOIN `tabSales Team` as cis on c.name=cis.parent            
        ORDER BY 
            c.name, ci.item_name, ci.rate,ci.qty ASC;
    """

    data = frappe.db.sql(query,as_dict=True)
    return data


def get_columns():
    return [    
        {"label": "COF ID", "fieldname": "c_name", "fieldtype": "Link", "options": "Customer Order Form", "width": 200},
        {"label": "COF Item Name", "fieldname": "ci_item_name", "fieldtype": "Data", "width": 200},
        {"label": "Qty", "fieldname": "ci_qty", "fieldtype": "Float", "width": 100},
        {"label": "Rate", "fieldname": "ci_rate", "fieldtype": "Currency", "width": 100},
        {"label": "Amount", "fieldname": "ci_amount", "fieldtype": "Currency", "width": 100},
        {"label": "Supplier", "fieldname": "ci_supplier", "fieldtype": "Link","options":"Supplier", "width": 100},
        {"label": "Supplier Item Name", "fieldname": "ci_supplier_item", "fieldtype": "Data", "width": 200},
        {"label": "Supplier Rate", "fieldname": "ci_supplier_rate", "fieldtype": "Currency", "width": 100},
        {"label": "Supplier Amount", "fieldname": "ci_supplier_amount", "fieldtype": "Currency", "width": 100},
        {"label": "Difference Amount", "fieldname": "difference_amount", "fieldtype": "Currency", "width": 100},
        {"label": "Sales Person", "fieldname": "cis_sales_person", "fieldtype": "Link","options":"Sales Person", "width": 150}
	]
