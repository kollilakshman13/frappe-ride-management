# Copyright (c) 2024, lakshman and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    data_result = data(filters)
    columns = get_columns()
    item_totals = {}
    for d in data_result:
        item_name = d["ci_item_name"]
        selling_amount = d["ci_amount"]
        buying_amount = d["supplier_quotation_item_amount"]
        difference_amount = d["difference_amount"]
        
        if item_name not in item_totals:
            item_totals[item_name] = {"selling_amount": 0, "buying_amount": 0, "difference_amount": 0}
        
        item_totals[item_name]["selling_amount"] += selling_amount
        item_totals[item_name]["buying_amount"] += buying_amount
        item_totals[item_name]["difference_amount"] += difference_amount

    chart = {
        "data": {
            "xlabel": "Items",
            "ylabel": "Amount", 
            "labels": list(item_totals.keys()), 
            "datasets": [
                {
                    "name": "Total Selling Amount",
                    "values": [item_totals[item]["selling_amount"] for item in item_totals]
                },
                {
                    "name": "Total Buying Amount",
                    "values": [item_totals[item]["buying_amount"] for item in item_totals]
                },
                {
                    "name": "Total Difference Amount",
                    "values": [item_totals[item]["difference_amount"] for item in item_totals]
                }
            ]
        },
        "type": "bar"
    }

    return columns, data_result, None, chart

def data(filters=None):
    conditions = " "
    values = {}

    if filters:
        if filters.get("from"):
            conditions += " AND c.transaction_date >= %(from)s"
            values["from"] = filters["from"]
        if filters.get("to"):
            conditions += " AND c.transaction_date <= %(to)s"
            values["to"] = filters["to"]
        if filters.get("customer_name"):
            conditions += " AND c.party_name LIKE %(customer_name)s"
            values["customer_name"] = f"%{filters['customer_name']}%"    
        if filters.get("name"):
            conditions += " AND c.name LIKE %(name)s"
            values["name"] = f"%{filters['name']}%"
        if filters.get("supplier_name"):
            conditions += " AND sq.supplier LIKE %(supplier_name)s"
            values["supplier_name"] = f"%{filters['supplier_name']}%"     
        if filters.get("item"):
            conditions += " AND ci.item_code LIKE %(item)s"
            values["item"] = f"%{filters['item']}%"
        if filters.get("brand"):
            conditions += " AND ci.brand LIKE %(brand)s"
            values["brand"] = f"%{filters['brand']}%"    
        if filters.get("sales"):
            conditions += " AND cis.sales_person LIKE %(sales)s"
            values["sales"] = f"%{filters['sales']}%"
        if filters.get("company"):
            conditions += " AND c.company_address_name LIKE %(company)s"
            values["company"] = f"%{filters['company']}%"      

    query = """
        SELECT 
            c.name AS c_name,
            c.party_name AS c_party_name,
            sq.supplier AS sq_supplier,
            c.transaction_date AS c_transaction_date,
            ci.item_name AS ci_item_name,
            ci.item_code AS ci_item_code,
            ci.item_group AS ci_item_group,
            ci.brand AS ci_brand,
            ci.qty AS ci_qty,
            ci.rate AS ci_rate,
            ci.amount AS ci_amount,
            si.rate AS supplier_quotation_item_rate,
            si.amount AS supplier_quotation_item_amount,
            ci.amount - si.amount AS difference_amount,
            cis.sales_person AS cis_sales_person
            
        FROM 
            `tabCustomer Order Form` AS c 
        LEFT JOIN `tabCustomer Order Item` AS ci ON c.name = ci.parent
        LEFT JOIN `tabSales Team` AS cis ON c.name=cis.parent

        LEFT JOIN `tabQuotation` as q on c.quotation=q.name
        LEFT JOIN `tabQuotation Item` as qi on q.name=qi.parent
            AND ci.item_name = qi.item_name 
            AND ci.qty = qi.qty 
            AND ci.item_code = qi.item_code 
            AND ci.description = qi.description

        LEFT JOIN `tabOpportunity` AS opp on q.opportunity=opp.name
        LEFT JOIN `tabOpportunity Item` as oi on opp.name=oi.parent
            AND ci.item_name = oi.item_name 
            AND ci.qty = oi.qty 
            AND ci.item_code = oi.item_code 
            AND ci.description = oi.description
            

        LEFT JOIN `tabSupplier Quotation` AS sq ON opp.name=sq.opportunity
        LEFT JOIN  `tabSupplier Quotation Item` AS si ON sq.name = si.parent 
           AND ci.item_name = si.item_name 
           AND ci.item_code = si.item_code
           AND ci.qty = si.qty 
           AND ci.item_code = si.item_code 
           AND ci.description = si.description 
            WHERE si.recommended = 1
        {}
        ORDER BY 
            c.name, ci.item_name, ci.rate, ci.qty ASC;
    """.format(conditions)

    data1 = frappe.db.sql(query,values,as_dict=True)
    return data1

def get_columns():
    return [
        {"label": "Customer Order Form ID", "fieldname": "c_name", "fieldtype": "Link", "options": "Customer Order Form", "width": 200},
        {"label": "Customer Name", "fieldname": "c_party_name", "fieldtype": "Link", "options": "Customer", "width": 200},
        {"label": "Supplier", "fieldname": "sq_supplier", "fieldtype": "Link", "options": "Supplier", "width": 200},
        {"label": "Date", "fieldname": "c_transaction_date", "fieldtype": "Date", "width": 100},
        {"label": "Item Name", "fieldname": "ci_item_name", "fieldtype": "Link", "options": "Item", "width": 200},
        {"label": "Item Code", "fieldname": "ci_item_code", "fieldtype": "Data", "width": 200},
        {"label": "Item Group", "fieldname": "ci_item_group", "fieldtype": "Data", "width": 150},
        {"label": "Brand", "fieldname": "ci_brand", "fieldtype": "Data", "width": 100},
        {"label": "Qty", "fieldname": "ci_qty", "fieldtype": "Float", "width": 100},
        {"label": "Selling Rate", "fieldname": "ci_rate", "fieldtype": "Currency", "width": 150},
        {"label": "Selling Amount", "fieldname": "ci_amount", "fieldtype": "Currency", "width": 150},
        {"label": "Buying Rate", "fieldname": "supplier_quotation_item_rate", "fieldtype": "Currency", "width": 150},
        {"label": "Buying Amount", "fieldname": "supplier_quotation_item_amount", "fieldtype": "Currency", "width": 150},
        {"label": "Difference Amount", "fieldname": "difference_amount", "fieldtype": "Currency", "width": 150},
        {"label": "Sales Person", "fieldname": "cis_sales_person", "fieldtype": "Link", "options": "Sales Person", "width": 150}
    ]
