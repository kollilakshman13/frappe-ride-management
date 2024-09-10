# Copyright (c) 2023, lakshman and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class Vehicles(WebsiteGenerator):
	pass



# data = frappe.db.sql(f"""
#     SELECT eg.name, ft.field_name, ft.condition, ft.value
#     FROM `tabVehicles` AS eg
#     LEFT JOIN `tabRide Order Filter` AS ft ON eg.name = ft.parent
#     WHERE eg.name = 'Honda' 
# """)
# if data:
#     details = []
#     for row in data:
#         field_name = row[1]
#         condition = row[2]
#         value = row[3]
#         value = value.replace('\n', ', ')
#         # Split values and format them
#         # frappe.msgprint(value.split(','))
#         value_list = [v.strip() for v in value.split(',') if v.strip()]
#         formatted_values = ", ".join([f"'{v}'" for v in value_list])
#         details.append(f" `tab{field_name}`.name {condition} ({formatted_values})")
#         print(details)
