# Copyright (c) 2024, lakshman and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    return get_columns(), get_data(filters)


def get_data(filters):
    _from, to = filters.get('from'), filters.get('to')

    conditions = "AND 1+1"
    if filters.get("Vehicle"):
        conditions += f" AND Vehicle LIKE'{filters.get('Vehicle')}' "
    if filters.get("total_amount"):
        conditions += f" AND total_amount='{filters.get('total_amount')}' "
    if filters.get("status"):
        conditions += f" AND status='{filters.get('status')}' "

    data = frappe.db.sql(f""" SELECT vehicle, customer_name, status, pick, phone, rate, distance, total_amount FROM `tabRide order` WHERE (creation BETWEEN '{_from}' AND '{to}') {conditions};""")

    return data


def get_columns():
    return [
        "vehicle:Link/Vehicles:100",
        "customer_name:Data:150",
        "Status:Data:100",
        "Pick:Small Text:300",
        "phone:Data:100",
        "Rate:Currency:100",
        "Distance:Float",
        "Amount:Currency:100"
        
    ]
