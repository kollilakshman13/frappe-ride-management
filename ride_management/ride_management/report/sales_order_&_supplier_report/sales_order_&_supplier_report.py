# Copyright (c) 2024, lakshman and contributors
# For license information, please see license.txt

import frappe
# def execute(filters=None):
#     data_result = data(filters)
#     columns = get_columns()
#     #chart = generate_chart(data_result)
#     return columns, data_result#, None ,chart

# def data(filters=None):
#     conditions = ""
#     values = {}

#     if filters:
#         if filters.get("from"):
#             conditions += " AND so.transaction_date >= %(from)s"
#             values["from"] = filters["from"]
#         if filters.get("to"):
#             conditions += " AND so.transaction_date <= %(to)s"
#             values["to"] = filters["to"]
#         if filters.get("name"):
#             conditions += " AND so.name IN %(name)s"
#             values["name"] = filters['name'] 
#         if filters.get("item"):
#             conditions += " AND soi.item_code IN %(item)s"
#             values["item"] = filters['item']   
#         if filters.get("item_group"):
#             conditions += " AND soi.item_group IN %(item_group)s"
#             values["item_group"] = filters['item_group']  
#         if filters.get("brand"):
#             conditions += " AND soi.brand IN %(brand)s"
#             values["brand"] = filters['brand']

#     query = """
#         SELECT  
#             so.name AS so_name,
#             sq.name AS sq_name,
#             so.customer AS so_customer,
#             sq.supplier AS sq_supplier,
#             so.transaction_date AS so_transaction_date,
#             soi.item_code AS soi_item_code,
#             soi.item_group AS soi_item_group,
#             soi.brand AS soi_brand,
#             soi.qty AS soi_qty,
#             soi.rate AS soi_rate,
#             soi.amount AS soi_amount,
#             si.rate AS supplier_quotation_item_rate,
#             si.amount AS supplier_quotation_item_amount,
#             soi.amount - si.amount AS difference_amount,
#             cis.sales_person AS cis_sales_person
#         FROM 
#             `tabSales Order` AS so
#         LEFT JOIN `tabSales Order Item` soi on so.name=soi.parent
#         LEFT JOIN `tabSales Team` AS cis ON so.name=cis.parent
#         LEFT JOIN `tabCustomer Order Form`  AS c on so.cof_id=c.name
#         LEFT JOIN `tabCustomer Order Item` AS ci ON c.name = ci.parent
#             AND soi.qty = ci.qty 
#             AND soi.item_code = ci.item_code 
#             AND soi.description = ci.description
#         LEFT JOIN `tabQuotation` as q on c.quotation=q.name
#         LEFT JOIN `tabQuotation Item`as qi on q.name=qi.parent
#             AND soi.qty = qi.qty 
#             AND soi.item_code = qi.item_code 
#             AND soi.description = qi.description
#         LEFT JOIN `tabOpportunity` AS opp on q.opportunity=opp.name
#         LEFT JOIN `tabOpportunity Item`as oi on opp.name=oi.parent
#             AND soi.qty = oi.qty 
#             AND soi.item_code = oi.item_code 
#             AND soi.description = oi.description 
#         LEFT JOIN `tabSupplier Quotation` AS sq ON opp.name=sq.opportunity
#         LEFT JOIN `tabSupplier Quotation Item` AS si ON sq.name = si.parent 
#             AND soi.item_code = si.item_code
#             AND soi.qty = si.qty 
#             AND soi.description = si.description 
#         WHERE si.recommended = 1  
#         {} 
#         GROUP BY 
#             so.name,soi.name,soi.idx 
#         ORDER BY 
#             so.name,sq.name,soi.item_code, soi.rate, soi.qty ASC 
#     """.format(conditions)
    
#     data = frappe.db.sql(query, values, as_dict=True)  
#     return data


# def get_columns():
#     return [
#         {"label": "Sales Order ID", "fieldname": "so_name", "fieldtype": "Link", "options": "Sales Order", "width": 200},
#         {"label": "Supplier ID", "fieldname": "sq_name", "fieldtype": "Link", "options": "Supplier Quotation", "width": 200},
#         {"label": "Customer", "fieldname": "so_customer", "fieldtype": "Link", "options": "Customer", "width": 200},
#         {"label": "Supplier Name", "fieldname": "sq_supplier", "fieldtype": "Link", "options": "Supplier", "width": 200},
#         {"label": "Date", "fieldname": "so_transaction_date", "fieldtype": "Date", "width": 100},
#         {"label": "Item Name", "fieldname": "soi_item_code", "fieldtype": "Link", "options": "Item", "width": 200},
#         {"label": "Sales Qty", "fieldname": "soi_qty", "fieldtype": "Float", "width": 100},
#         {"label": "Sales Rate", "fieldname": "soi_rate", "fieldtype": "Currency", "width": 150},
#         {"label": "Sales Amount", "fieldname": "soi_amount", "fieldtype": "Currency", "width": 150},
#         {"label": "Purchase Rate", "fieldname": "supplier_quotation_item_rate", "fieldtype": "Currency", "width": 150},
#         {"label": "Purchase Amount", "fieldname": "supplier_quotation_item_amount", "fieldtype": "Currency", "width": 150},
#         {"label": "Difference Amount", "fieldname": "difference_amount", "fieldtype": "Currency", "width": 150},
#         {"label": "Sales Person", "fieldname": "cis_sales_person", "fieldtype": "Link", "options": "Sales Person", "width": 150}
#     ]

# def generate_chart(data_result):
#     item_totals = {}
#     for d in data_result:
#         item_name = d["soi_item_code"]
#         sales_amount = d["soi_amount"]
#         purchase_amount = d["supplier_quotation_item_amount"]
#         difference_amount = d["difference_amount"]
        
#         if item_name not in item_totals:
#             item_totals[item_name] = {"sales_amount": 0, "purchase_amount": 0, "difference_amount": 0}
        
#         item_totals[item_name]["sales_amount"] += sales_amount
#         item_totals[item_name]["purchase_amount"] += purchase_amount
#         item_totals[item_name]["difference_amount"] += difference_amount
      
#     chart_data = {
#         "data": {
#             "xlabel": "Items",
#             "ylabel": "Amount", 
#             "labels": list(item_totals.keys()),
#             "datasets": [
#                 {
#                     "name": "Total Sales Amount",
#                     "values": [item_totals[item]["sales_amount"] for item in item_totals]
#                 },
#                 {
#                     "name": "Total Purchase Amount",
#                     "values": [item_totals[item]["purchase_amount"] for item in item_totals]
#                 },
#                 {
#                     "name": "Total Difference Amount",
#                     "values": [item_totals[item]["difference_amount"] for item in item_totals]
#                 }
#             ]
#         },
#         "type": "bar"
#     }
#     return chart_data

					
def execute(filters=None):
    selected_columns = filters.get("selected_columns") if filters else []
    columns = get_columns(selected_columns)
    data_result = data(filters, selected_columns)
    return columns, data_result

def data(filters=None, selected_columns=None):
    conditions = ""
    values = {}

    if filters:
        if filters.get("from"):
            conditions += " AND so.transaction_date >= %(from)s"
            values["from"] = filters["from"]
        if filters.get("to"):
            conditions += " AND so.transaction_date <= %(to)s"
            values["to"] = filters["to"]
        if filters.get("name"):
            conditions += " AND so.name IN %(name)s"
            values["name"] = filters['name'] 
        if filters.get("item"):
            conditions += " AND soi.item_code IN %(item)s"
            values["item"] = filters['item']   
        if filters.get("item_group"):
            conditions += " AND soi.item_group IN %(item_group)s"
            values["item_group"] = filters['item_group']  
        if filters.get("brand"):
            conditions += " AND soi.brand IN %(brand)s"
            values["brand"] = filters['brand']

    selected_columns_str = ", ".join([f"{col['fieldname']} AS {col['fieldname']}" for col in get_columns(selected_columns)])
    
    query = f"""
        SELECT  
            {selected_columns_str}
        FROM 
            `tabSales Order` AS so
        LEFT JOIN `tabSales Order Item` soi on so.name=soi.parent
        LEFT JOIN `tabSales Team` AS cis ON so.name=cis.parent
        LEFT JOIN `tabCustomer Order Form`  AS c on so.cof_id=c.name
        LEFT JOIN `tabCustomer Order Item` AS ci ON c.name = ci.parent
            AND soi.qty = ci.qty 
            AND soi.item_code = ci.item_code 
            AND soi.description = ci.description
        LEFT JOIN `tabQuotation` as q on c.quotation=q.name
        LEFT JOIN `tabQuotation Item`as qi on q.name=qi.parent
            AND soi.qty = qi.qty 
            AND soi.item_code = qi.item_code 
            AND soi.description = qi.description
        LEFT JOIN `tabOpportunity` AS opp on q.opportunity=opp.name
        LEFT JOIN `tabOpportunity Item`as oi on opp.name=oi.parent
            AND soi.qty = oi.qty 
            AND soi.item_code = oi.item_code 
            AND soi.description = oi.description 
        LEFT JOIN `tabSupplier Quotation` AS sq ON opp.name=sq.opportunity
        LEFT JOIN `tabSupplier Quotation Item` AS si ON sq.name = si.parent 
            AND soi.item_code = si.item_code
            AND soi.qty = si.qty 
            AND soi.description = si.description 
        WHERE si.recommended = 1  
        {conditions}
        GROUP BY 
            so.name,soi.name,soi.idx 
        ORDER BY 
            so.name,sq.name,soi.item_code, soi.rate, soi.qty ASC 
    """
    
    data = frappe.db.sql(query, values, as_dict=True)  
    return data

def get_columns(selected_columns=None):
    columns = [
        {"label": "Sales Order ID", "fieldname": "so_name", "fieldtype": "Link", "options": "Sales Order", "width": 200},
        {"label": "Supplier ID", "fieldname": "sq_name", "fieldtype": "Link", "options": "Supplier Quotation", "width": 200},
        {"label": "Customer", "fieldname": "so_customer", "fieldtype": "Link", "options": "Customer", "width": 200},
        {"label": "Supplier Name", "fieldname": "sq_supplier", "fieldtype": "Link", "options": "Supplier", "width": 200},
        {"label": "Date", "fieldname": "so_transaction_date", "fieldtype": "Date", "width": 100},
        {"label": "Item Name", "fieldname": "soi_item_code", "fieldtype": "Link", "options": "Item", "width": 200},
        {"label": "Sales Qty", "fieldname": "soi_qty", "fieldtype": "Float", "width": 100},
        {"label": "Sales Rate", "fieldname": "soi_rate", "fieldtype": "Currency", "width": 150},
        {"label": "Sales Amount", "fieldname": "soi_amount", "fieldtype": "Currency", "width": 150},
        {"label": "Purchase Rate", "fieldname": "supplier_quotation_item_rate", "fieldtype": "Currency", "width": 150},
        {"label": "Purchase Amount", "fieldname": "supplier_quotation_item_amount", "fieldtype": "Currency", "width": 150},
        {"label": "Difference Amount", "fieldname": "difference_amount", "fieldtype": "Currency", "width": 150},
        {"label": "Sales Person", "fieldname": "cis_sales_person", "fieldtype": "Link", "options": "Sales Person", "width": 150}
    ]
    
    if selected_columns:
        columns = [col for col in columns if col['fieldname'] in selected_columns]
    
    return columns











