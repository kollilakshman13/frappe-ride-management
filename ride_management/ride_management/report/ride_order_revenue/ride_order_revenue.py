# Copyright (c) 2024, lakshman and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = [
        {
            "fieldname": "vehicle",
            "label": "Vehicles",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "distance",
            "label": "Distance",
            "fieldtype": "Float",
            "width": 150
        },
        {
            "fieldname": "revenue",
            "label": "Revenue",
            "fieldtype": "Currency",
            "width": 150
        }  
    ]

    rides = frappe.get_all("Ride order", fields=["vehicle", "total_amount", "distance"])

    revenue_by_vehicle = {}

    for ride in rides:
        if ride.vehicle in revenue_by_vehicle:
            revenue_by_vehicle[ride.vehicle]["revenue"] += ride.total_amount
            revenue_by_vehicle[ride.vehicle]["distance"] += ride.distance
        else:
            revenue_by_vehicle[ride.vehicle] = {"revenue": ride.total_amount,  "distance": ride.distance}

    data = [{"vehicle": make, 
             "revenue": revenue["revenue"], 
             "distance": revenue["distance"]} 
             for make, revenue in revenue_by_vehicle.items()]

    num_records = filters.number_of_records if filters and filters.get("number_of_records") else 10
    chart1 = get_chart(data)
    return columns, data[:num_records], None, chart1, None

def get_chart(data):
    return {
        "data": {
            "labels": [d["vehicle"] for d in data],
            "datasets": [{
                "name": "Revenue by Vehicle",
                "values": [d["revenue"] for d in data]
                
            }]
        },
        "type": "bar"
    }


       
         

         
        
         
         
 
