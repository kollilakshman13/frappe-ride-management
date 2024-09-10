# Copyright (c) 2024, lakshman and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

#class Rideorder(Document):
	#pass

import frappe
from frappe import _
from frappe.model.document import Document
import json

class Rideorder(Document):
    def validate(self):
        if self.filters_json:
            try:
                filters = json.loads(self.filters_json)
                # Optionally validate the filter structure
                for filter_item in filters:
                    if not all(key in filter_item for key in ('fieldname', 'condition', 'value')):
                        frappe.throw(_('Invalid filter structure'))
            except json.JSONDecodeError:
                frappe.throw(_('Invalid JSON in filters'))
   

# from frappe.utils import get_url, nowdate
# import frappe

# @frappe.whitelist()
# def assign_task(doc_str, method=None):
#     doc = json.loads(doc_str)  
#     if doc.get('assign_to'):
#        assign_to_user(doc)
#        send_email_notification(doc)

# def assign_to_user(doc):
#     # Assign the task to the user
#     assignment = frappe.new_doc("ToDo")
#     assignment.owner = doc.assign_to
#     assignment.reference_type = "Task"
#     assignment.reference_name = doc.name
#     assignment.description = doc.subject
#     assignment.date = nowdate()
#     assignment.save(ignore_permissions=True)
#     frappe.db.commit()

# def send_email_notification(doc):
#     # Send an email notification to the assigned user
#     recipient = doc.assign_to
#     subject = f"New Task Assigned: {doc.name}"
#     message = f"""
#     <p>Dear {frappe.db.get_value("User", recipient, "first_name")},</p>
#     <p>You have been assigned a new task:</p>
#     <p><strong>{doc.subject}</strong></p>
#     <p>Due Date: {doc.exp_end_date}</p>
#     <p>Click <a href="{get_url()}/desk#Form/Task/{doc.name}">here</a> to view the task.</p>
#     <p>Regards,</p>
#     <p>{frappe.db.get_value("User", doc.modified_by, "full_name")}</p>
#     """
#     frappe.sendmail(
#         recipients=[recipient],
#         subject=subject,
#         message=message
#     )

# apps/ride_management/ride_management/doctype/ride_order/ride_order.py

import frappe
from frappe.utils import get_url, nowdate
@frappe.whitelist()
def assign_task(doc, method=None):
    # Ensure doc is an object of type Rideorder
    if isinstance(doc, dict):
        doc_name = doc.get('name')
        doc = frappe.get_doc("Ride order", doc_name)
    
    if doc.assign_to and not check_existing_assignment(doc):
        assign_to_user(doc)
        send_email_notification(doc)

def check_existing_assignment(doc):
    # Check if an assignment already exists for this document and user
    return frappe.db.exists("ToDo", {
        "owner": doc.assign_to,
        "reference_type": "Ride order",
        "reference_name": doc.name
    })

def assign_to_user(doc):
    assignment = frappe.new_doc("ToDo")
    assignment.owner = doc.assign_to
    assignment.reference_type = "Ride order"
    assignment.reference_name = doc.name
    assignment.description = doc.state
    assignment.date = nowdate()
    assignment.save(ignore_permissions=True)
    frappe.db.commit()

def send_email_notification(doc):
    recipient = doc.assign_to
    subject = f"New Task Assigned: {doc.name}"
    message = f"""
    <p>Dear {frappe.db.get_value("User", recipient, "first_name")},</p>
    <p>You have been assigned a new task:</p>
    <p><strong>{doc.state}</strong></p>
    <p>Due Date: {doc.city}</p>
    <p>Click <a href="{get_url()}/desk#Form/Ride order/{doc.name}">here</a> to view the task.</p>
    <p>Regards,</p>
    <p>{frappe.db.get_value("User", doc.modified_by, "full_name")}</p>
    """
    frappe.sendmail(
        recipients=[recipient],
        subject=subject,
        message=message
    )




# import frappe #####

# @frappe.whitelist()
# def share_ride_order(doc_name, user, read=0, write=0):
#     try:
#         # Check if a share already exists and update it
#         if frappe.db.exists('DocShare', {'user': user, 'share_name': doc_name, 'share_doctype': 'Ride order'}):
#             share_doc = frappe.get_doc('DocShare', {'user': user, 'share_name': doc_name, 'share_doctype': 'Ride order'})
#             share_doc.read = int(read)
#             share_doc.write = int(write)
            
#         else:
#             # Add a new share entry for the Ride Order document
#             frappe.share.add(
#                 doctype='Ride order',
#                 name=doc_name,
#                 user=user,
#                 read=int(read),
#                 write=int(write)
#             )
        
#         # Handle the submit permission separately if needed
#         # if submit:
#         #     frappe.permissions.add_user_permission('Ride order', doc_name, user)
        
#         return 'success'
#     except Exception as e:
#         frappe.log_error(message=str(e), title="Share Ride order Error")
#         return 'error'




# @frappe.whitelist()
# def share_ride_order(doc_name, user, read=0, write=0):
#     try:
#         # Check if a share already exists and update it
#         if frappe.db.exists('DocShare', {'user': user, 'share_name': doc_name, 'share_doctype': 'Ride order'}):
#             share_doc = frappe.get_doc('DocShare', {'user': user, 'share_name': doc_name, 'share_doctype': 'Ride order'})
#             share_doc.read = int(read)
#             share_doc.write = int(write)
#             share_doc.save()
#         else:
#             # Add a new share entry for the Ride Order document
#             frappe.share.add(
#                 doctype='Ride order',
#                 name=doc_name,
#                 user=user,
#                 read=int(read),
#                 write=int(write)
#             )

#         return 'success'
#     except Exception as e:
#         frappe.log_error(message=str(e), title="Share Ride order Error")
#         return 'error'

# @frappe.whitelist()
# def unshare_ride_order(doc_name, users):
#     try:
#         for user in users:
#             if frappe.db.exists('DocShare', {'user': user, 'share_name': doc_name, 'share_doctype': 'Ride order'}):
#                 frappe.delete_doc('DocShare', {'user': user, 'share_name': doc_name, 'share_doctype': 'Ride order'})
        
#         return 'success'
#     except Exception as e:
#         frappe.log_error(message=str(e), title="Unshare Ride order Error")
#         return 'error'





import frappe

@frappe.whitelist()
def share_ride_order(doc_name, user, read=0, write=0):
    try:
        if frappe.db.exists('DocShare', {'user': user, 'share_name': doc_name, 'share_doctype': 'Ride order'}):
            share_doc = frappe.get_doc('DocShare', {'user': user, 'share_name': doc_name, 'share_doctype': 'Ride order'})
            share_doc.read = int(read)
            share_doc.write = int(write)
            share_doc.save()
        else:
            frappe.share.add(
                doctype='Ride order',
                name=doc_name,
                user=user,
                read=int(read),
                write=int(write)
            )
        return 'success'
    except Exception as e:
        frappe.log_error(message=str(e), title="Share Ride Order Error")
        return 'error'

@frappe.whitelist()
def unshare_ride_order(doc_name, user):
    try:
        if frappe.db.exists('DocShare', {'user': user, 'share_name': doc_name, 'share_doctype': 'Ride order'}):
            frappe.db.delete('DocShare', {'user': user, 'share_name': doc_name, 'share_doctype': 'Ride order'})
        return 'success'
    except Exception as e:
        frappe.log_error(message=str(e), title="Unshare Ride Order Error")
        return 'error'

@frappe.whitelist()
def sync_sharing_permissions(doc_name, share_permissions):
    try:
        # Convert share_permissions to a list of dictionaries
        if not isinstance(share_permissions, list):
            share_permissions = frappe.parse_json(share_permissions)
        
        # Get the current shared users
        current_shared_users = frappe.get_all('DocShare', filters={'share_name': doc_name, 'share_doctype': 'Ride order'}, fields=['user'])
        current_shared_users = [user['user'] for user in current_shared_users]

        # Get the users from the share_permissions child table
        new_shared_users = [row['user'] for row in share_permissions]

        # Determine which users to unshare
        users_to_unshare = list(set(current_shared_users) - set(new_shared_users))

        # Unshare the document from users not in the new shared users list
        for user in users_to_unshare:
            unshare_ride_order(doc_name, user)

        # Share the document with the new shared users
        for row in share_permissions:
            share_ride_order(doc_name, row['user'], row.get('read_permission', 0), row.get('write_permission', 0))

        return 'success'
    except Exception as e:
        frappe.log_error(message=str(e), title="Sync Sharing Permissions Error")
        return 'error'

@frappe.whitelist()
def get_shared_users(doc_name):
    try:
        shared_docs = frappe.get_all('DocShare', filters={'share_name': doc_name, 'share_doctype': 'Ride order'}, fields=['user', 'read', 'write'])

        return shared_docs
    except Exception as e:
        frappe.log_error(message=str(e), title="Get Shared Users Error")
        return []




# val = frappe.get_all('Ride order', filters={"name": "RO-11-07-2024-0147"}, fields=['filters_json'])
# print(val)

# import json
# ride_order = frappe.get_all('Ride order', filters={"name": "RO-11-07-2024-0147"}, fields=['filters_json'])
# if ride_order:
#     print("Filters JSON:", ride_order[0].get('filters_json'))
# else:
#     print("Ride order not found")
# # Extract and print only the values of each filter
# filters_json = json.loads(ride_order[0]['filters_json'])
# for filter_item in filters_json:
#     print(f"Values for field '{filter_item['fieldname']}': {filter_item['value']}")
    #  print(f"Field: {filter_item['fieldname']}, Condition: {filter_item['condition']}, Value: {filter_item['value']}")




# import frappe
# import json
     
# # Fetch all Ride Order documents that match certain criteria (you can customize the filter criteria)
# ride_orders = frappe.get_all('Ride order', filters={}, fields=['name', 'filters_json'])
     
# # Loop through each Ride Order document
# for ride in ride_orders :
#     filters_json = ride.get('filters_json')
#     name = ride.get('name')
     
#         # Check if filters_json exists and is not empty
#     if filters_json:
#         try:
#             # Parse the JSON string into a Python list
#             filters_list = json.loads(filters_json)
    
#             # Process the filters
#             print(f"Ride Order: {name}")
#             for filter_item in filters_list:
#                 fieldname = filter_item.get('fieldname')
#                 condition = filter_item.get('condition')
#                 values = filter_item.get('value')
    
#                     # Print or process each filter item
#                 print(f"  {fieldname}  {condition}  {values}")
#         except json.JSONDecodeError:
#             print(f"Error decoding JSON for Ride Order: {name}")
#     else:
#         print(f"No filters found for Ride Order: {name}")





# import frappe
# import json

# # Fetch all Ride Order documents
# ride_orders = frappe.get_all('Ride order', filters={}, fields=['name', 'filters_json'])

# # Loop through each Ride Order document
# for ride in ride_orders:
#     filters_json = ride.get('filters_json')
#     name = ride.get('name')

#     # Check if filters_json exists and is not empty
#     if filters_json:
#         try:
#             # Parse the JSON string into a Python list
#             filters_list = json.loads(filters_json)
            
#             # Construct SQL WHERE clause
#             where_clauses = []
#             values = []

#             for filter_item in filters_list:
#                 fieldname = filter_item.get('fieldname')
#                 condition = filter_item.get('condition')
#                 filter_values = filter_item.get('value')
                
#                 # Ensure column name exists in the database schema
#                 if frappe.db.has_column('Ride order', fieldname):
#                     # Construct appropriate SQL condition
#                     if condition in ['in', 'not in']:
#                         placeholder = ', '.join(['%s'] * len(filter_values))
#                         where_clauses.append(f"`{fieldname}` {condition} ({placeholder})")
#                         values.extend(filter_values)
#                     else:
#                         where_clauses.append(f"`{fieldname}` {condition} %s")
#                         values.append(filter_values[0])
#                 else:
#                     print(f"Column '{fieldname}' does not exist in 'Ride order' table")

#             if where_clauses:
#                 # Join all conditions with AND
#                 where_clause = ' AND '.join(where_clauses)
                
#                 # Final SQL query
#                 query = f"SELECT * FROM `tabRide order` WHERE {where_clause}"
#                 print(f"Executing SQL: {query} with values {values}")
                
#                 # Execute the SQL query
#                 results = frappe.db.sql(query, values, as_dict=True)
                
#                 # Process the results
#                 for result in results:
#                     print(result)
#             else:
#                 print(f"No valid filters found for Ride Order: {name}")
                
#         except json.JSONDecodeError:
#             print(f"Error decoding JSON for Ride Order: {name}")
#     else:
#         print(f"No filters found for Ride Order: {name}")




# data = frappe.db.sql("""
#     SELECT v.name, f.field_name,f.condition,f.value
#         FROM `tabVehicles` AS v
#         LEFT JOIN `tabRide Order Filter` AS f ON v.name = f.parent where v.name='Car0002'
#     """)
# print(data)


# data = frappe.db.sql("""
#     SELECT v.name, f.field_name, f.condition, f.value
#     FROM `tabVehicles` AS v
#     LEFT JOIN `tabRide Order Filter` AS f ON v.name = f.parent
#     WHERE v.name = 'Car0001'
# """)

# # Process the data to create the formatted string
# if data:
#     details = []
#     for row in data:
#         field_name = row[1]
#         condition = row[2]
#         values = row[3]
#         # Split values and format them
#         print([f"'{v.strip()}'" for v in values.split(',')])
#         formatted_values = ", ".join([f"'{v.strip()}'" for v in values.split(',')])
#         print(formatted_values)
#         details.append(f" `tab{field_name}` {condition} ({formatted_values})")

#     formatted_output = " AND ".join(details)
#     print(formatted_output)
# else:
#     print("No data found for the specified vehicle.")








