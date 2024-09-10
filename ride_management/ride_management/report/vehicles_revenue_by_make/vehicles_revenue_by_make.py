# Copyright (c) 2024, lakshman and contributors
# For license information, please see license.txt
#from erpnext.erpnext.accounts.doctype.account.chart_of_accounts.chart_of_accounts import get_chart
import frappe
from frappe import _


def execute(filters=None):
    columns = [
        {
            "fieldname": "vehicle",
            "label": "Vehicle",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "revenue",
            "label": "Revenue",
            "fieldtype": "Currency",
            "width": 150
        }
    ]

    rides = frappe.get_all("Ride Booking", fields=["vehicle", "total_amount"])

    revenue_by_vehicle = {}

    

    for ride in rides:
        if ride.vehicle in revenue_by_vehicle:
           revenue_by_vehicle[ride.vehicle] += int(ride.total_amount)
        else:
           revenue_by_vehicle[ride.vehicle] = int(ride.total_amount)

    data = [{"vehicle": make, "revenue": revenue} for make, revenue in revenue_by_vehicle.items()]

    num_records = filters.number_of_records if filters and filters.get("number_of_records") else 10
    chart= get_chart( data)

    return columns, data[:num_records],None, chart, None

def get_chart(data):
    return {
        "data": {
            "labels": [d["vehicle"] for d in data],
            "datasets": [{
                "name": "Revenue by Vehicle",
                "values": [d["revenue"] for d in data]
            }]
        },
        "type": "pie"
        #"type":"bar"
        #"type":"line"
        #"type":"heatmap"
        #"type":"donut"
        #"type":"percentage"
    }
