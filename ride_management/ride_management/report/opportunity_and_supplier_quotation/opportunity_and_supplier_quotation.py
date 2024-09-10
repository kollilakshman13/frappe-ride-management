# Copyright (c) 2024, lakshman and contributors
# For license information, please see license.txt

#import frappe
from frappe import _
import frappe

import frappe

def execute(filters=None):
    return get_columns(), get_data(filters)

def get_data(filters=None):
    conditions = "WHERE 1=1"
    values = {}

    if filters:
        if filters.get("from"):
            conditions += " AND opp.transaction_date >= %(from)s"
            values["from"] = filters["from"]
        if filters.get("to"):
            conditions += " AND opp.transaction_date <= %(to)s"
            values["to"] = filters["to"]
        if filters.get("customer_name"):
            conditions += " AND opp.customer_name LIKE %(customer_name)s"
            values["customer_name"] = f"%{filters['customer_name']}%"    
        if filters.get("name"):
            conditions += " AND opp.name LIKE %(name)s"
            values["name"] = f"%{filters['name']}%"
        if filters.get("item"):
            conditions += " AND oi.item_name LIKE %(item)s"
            values["item"] = f"%{filters['item']}%"
        if filters.get("supplier"):
            conditions += " AND sq.supplier LIKE %(supplier)s"
            values["supplier"] = f"%{filters['supplier']}%"    


    query = """
        SELECT 
            opp.name AS opportunity_id,
            opp.customer_name,
            opp.transaction_date,
            oi.item_name,
            oi.brand,
            oi.qty,
            oi.rates,
            oi.amounts,
            oi.item_group,
            opp.sales_stage,
            sq.name AS supplier_quotation_name,
            sq.supplier,
            sq.transaction_date AS supplier_quotation_transaction_date,
            si.item_name AS supplier_quotation_item_name,
            si.qty AS supplier_quotation_item_qty,
            si.rate AS supplier_quotation_item_rate,
            si.amount AS supplier_quotation_item_amount
        FROM 
            `tabOpportunity` AS opp
        LEFT JOIN  `tabOpportunity Item` AS oi ON opp.name = oi.parent
        LEFT JOIN `tabSupplier Quotation` AS sq ON opp.name = sq.opportunity
        LEFT JOIN  `tabSupplier Quotation Item` AS si ON sq.name = si.parent 
           AND oi.item_name = si.item_name 
           AND oi.qty = si.qty 
           AND oi.item_code=si.item_code 
           AND oi.description= si.description
        {}
        
        ORDER BY 
            opp.name, oi.item_name, oi.rates,si.rate, si.item_name ASC;
    """.format(conditions)

    data = frappe.db.sql(query, values)
    return data

def get_columns():
    return [
        {"label": "Opportunity ID", "fieldname": "opportunity_id", "fieldtype": "Link", "options": "Opportunity", "width": 200},
        {"label": "Customer Name", "fieldname": "customer_name", "fieldtype": "Link", "options": "Customer", "width": 200},
        {"label": "Transaction Date", "fieldname": "transaction_date", "fieldtype": "Date", "width": 200},
        {"label": "Item Name", "fieldname": "item_name", "fieldtype": "Data", "width": 200},
        {"label": "Brand", "fieldname": "brand", "fieldtype": "Link", "options": "Brand", "width": 200},
        {"label": "Item Qty", "fieldname": "qty", "fieldtype": "Float", "width": 100},
        {"label": "Rate", "fieldname": "rates", "fieldtype": "Currency", "width": 100},
        {"label": "Amount", "fieldname": "amounts", "fieldtype": "Currency", "width": 100},
        {"label": "Item Group", "fieldname": "item_group", "fieldtype": "Data", "width": 100},
        {"label": "Sales Stage", "fieldname": "sales_stage", "fieldtype": "Data", "width": 100},
        {"label": "Supplier Quotation Name", "fieldname": "supplier_quotation_name", "fieldtype": "Data", "width": 200},
        {"label": "Supplier", "fieldname": "supplier", "fieldtype": "Link", "options": "Supplier", "width": 200},
        {"label": "Supplier Quotation Transaction Date", "fieldname": "supplier_quotation_transaction_date", "fieldtype": "Date", "width": 100},
        {"label": "Supplier Quotation Item Name", "fieldname": "supplier_quotation_item_name", "fieldtype": "Data", "width": 200},
        {"label": "Supplier Quotation Item Qty", "fieldname": "supplier_quotation_item_qty", "fieldtype": "Float", "width": 100},
        {"label": "Supplier Quotation Item Rate", "fieldname": "supplier_quotation_item_rate", "fieldtype": "Currency", "width": 100},
        {"label": "Supplier Quotation Item Amount", "fieldname": "supplier_quotation_item_amount", "fieldtype": "Currency", "width": 100}
    ]




#        LEFT JOIN
#            `tabOpportunity Item` AS item ON opp.name = item.parent    
#        LEFT JOIN
#            `tabSupplier Quotation` AS sq ON opp.name = sq.opportunity 
#        LEFT JOIN
#            `tabSupplier Quotation Item` AS it ON  sq.name=it.parent  AND it.item_name = item.item_name
#        GROUP BY 
#            item.name


#         item.brand,
#         item.qty AS item_qty,
#        --item.rates AS item_rates,
#        --item.amounts AS item_amounts,
#        --item.item_group,
#        --opp.sales_stage,
#       -- sq.name AS supplier_quotation_name,
#       -- sq.supplier,
#        --sq.transaction_date AS sq_transaction_date,
#        --it.item_name AS supplier_quotation_item_name,
#        --it.qty AS sq_item_qty,
#        --it.rate AS sq_item_rate,
#        --it.amount AS sq_item_amount