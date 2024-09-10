# Copyright (c) 2024, lakshman and contributors
# For license information, please see license.txt

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
            conditions += " AND item.item_name LIKE %(item)s"
            values["item"] = f"%{filters['item']}%"

    query = """
        SELECT 
            opp.name AS opportunity_name,
            opp.customer_name,
            opp.transaction_date,
            item.item_name,
            item.brand,
            item.qty AS item_qty,
            item.rates AS item_rates,
            item.amounts AS item_amount,
            item.item_group,
            opp.sales_stage,
            quo.name AS quotation_name,
            quo.customer_name AS quotation_customer_name,
            qi.item_name AS quotation_item_name,
            qi.qty AS quotation_item_qty,
            qi.rate AS quotation_item_rate,
            qi.amount AS quotation_item_amount
        FROM 
            `tabOpportunity` AS opp
        LEFT JOIN 
            `tabOpportunity Item` AS item ON opp.name = item.parent
        LEFT JOIN 
            `tabQuotation` AS quo ON opp.name = quo.opportunity
        LEFT JOIN 
            `tabQuotation Item` AS qi ON quo.name = qi.parent 
            AND item.item_name = qi.item_name 
            AND item.qty=qi.qty 
            AND item.item_code=qi.item_code 
            AND item.description= qi.description    
        {}
               
        ORDER BY 
            opp.name, item.item_name,item.rates,qi.item_name,qi.rate;
    """.format(conditions)

    data = frappe.db.sql(query, values)
    return data

def get_columns():
    return [
        {"label": "Opportunity Name", "fieldname": "opportunity_name", "fieldtype": "Link", "options": "Opportunity", "width": 200},
        {"label": "Customer Name", "fieldname": "customer_name", "fieldtype": "Link", "options": "Customer", "width": 200},
        {"label": "Transaction Date", "fieldname": "transaction_date", "fieldtype": "Date", "width": 100},
        {"label": "Item Name", "fieldname": "item_name", "fieldtype": "Data", "width": 200},
        {"label": "Brand", "fieldname": "brand", "fieldtype": "Link", "options": "Brand", "width": 200},
        {"label": "Item Qty", "fieldname": "item_qty", "fieldtype": "Float", "width": 100},
        {"label": "Item Rates", "fieldname": "item_rates", "fieldtype": "Currency", "width": 100},
        {"label": "Item Amount", "fieldname": "item_amount", "fieldtype": "Currency", "width": 100},
        {"label": "Item Group", "fieldname": "item_group", "fieldtype": "Data", "width": 100},
        {"label": "Sales Stage", "fieldname": "sales_stage", "fieldtype": "Data", "width": 100},
        {"label": "Quotation Name", "fieldname": "quotation_name", "fieldtype": "Link", "options": "Quotation", "width": 200},
        {"label": "Quotation Customer", "fieldname": "quotation_customer_name", "fieldtype": "Link", "options": "Customer", "width": 200},
        {"label": "Quotation Item Name", "fieldname": "quotation_item_name", "fieldtype": "Data", "width": 200},
        {"label": "Qty", "fieldname": "quotation_item_qty", "fieldtype": "Float", "width": 100},
        {"label": "Rates", "fieldname": "quotation_item_rate", "fieldtype": "Currency", "width": 100},
        {"label": "Amount", "fieldname": "quotation_item_amount", "fieldtype": "Currency", "width": 100}
    ]
