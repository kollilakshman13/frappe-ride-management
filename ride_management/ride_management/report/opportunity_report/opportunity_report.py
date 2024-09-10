# Copyright (c) 2024, lakshman and contributors
# For license information, please see license.txt

import frappe

import frappe

def execute(filters=None):
    if filters is None:
        filters = {}
    return get_columns(), get_opportunity_data(filters)


def get_opportunity_data(filters):
    conditions = "WHERE 1=1"
    values = {}

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

    sql_query = f"""
        SELECT 
            opp.name AS opportunity_name,
            opp.customer_name,
            opp.transaction_date,
            opp.sales_stage,
            item.item_name,
            item.qty,
            item.rates,
            item.amounts,
            item.brand,
            item.item_group
        FROM 
            `tabOpportunity` AS opp
        LEFT JOIN 
            `tabOpportunity Item` AS item ON opp.name = item.parent
        {conditions}
    """
    data = frappe.db.sql(sql_query,values)
    return data

def get_columns():
    return [
        "Opportunity ID:Data:200",
        "Customer name:Data:300",
        "Created Date:Date:100",
        "Item Name:Data:300",
        "Brand:Link/Brand:100",
        "Item qty:Float:100",
        "Item Rate:Currency:100",
        "Item Amount:Currency:100",
        "Item Group:Link/Item Group:100",
        "Sales Stage:Data:100",
    ]




