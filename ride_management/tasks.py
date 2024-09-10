import frappe
import string 
import random

def all ():
    pass

def cron():
    
    pass
    #print("\n\n Inserting new note \n\n")
    
    #letters=string.ascii_letters
    #note=" ".join(random.choice(letters)for i in range (20))

    #New_note=frappe.get_doc({"doctype":"Note","title": note })

    #New_note.insert()
    #frappe.db.commit()

import frappe
from frappe.utils import now_datetime

# def send_remainder_notifications():
#     # Get current time
#     current_time = now_datetime()
    
#     # Fetch all Call List entries where the remainder is equal to the current time
#     call_list = frappe.get_all('Call List', filters={
#         'remainder': current_time
#     })

#     for call in call_list:
#         # Fetch the full document
#         call_doc = frappe.get_doc('Call List', call.name)
        
#         # Define the message
#         message = f"Reminder: You have a call scheduled with {call_doc.contact_person} at {call_doc.remainder}."
        
#         # Send the system notification
#         frappe.publish_realtime(
#             event='msgprint',
#             message=message,
#             user=call_doc.owner  # Send notification to the document owner
#         )

#         # Optionally, send an email as well
#         frappe.sendmail(
#             recipients=[call_doc.owner],
#             subject="Call Reminder",
#             message=message
#         )

# # Schedule this function to run every minute
# send_remainder_notifications()
# def send_remainder_notifications():
#     current_time = frappe.utils.now_datetime()

#     # Fetch Call List records where remainder time is due and notification has not been sent
#     due_calls = frappe.get_all('Call List', filters={
#         'remainder': ['<=', current_time],  # Ensure remainder is less than or equal to the current time
#         'remainder': 0    # Ensure notification has not been sent
#     }, fields=['name', 'owner'])

#     for call in due_calls:
#         # Create and send notification
#         notification_title = "Call Reminder"
#         notification_message = f"Reminder for your scheduled call in Call List {call['name']}."

#         # Send system notification
#         frappe.get_doc({
#             'doctype': 'Notification Log',
#             'subject': notification_title,
#             'email_content': notification_message,
#             'for_user': call['owner']
#         }).insert(ignore_permissions=True)

#         # Mark the remainder notification as sent
#         frappe.db.set_value('Call List', call['name'], 'remainder', 1)

#     frappe.db.commit()

# # Ensure the function is registered
# send_remainder_notifications()

# import frappe
# from frappe.utils import now_datetime

# def send_reminder_notifications():
#     current_time = now_datetime()
    
#     # Fetch all call list entries where the reminder time is due and notification is not yet sent
#     call_lists = frappe.get_all("Call List", filters={
#         "remainder": ["<=", current_time],
#         "remainder_notification_sent": 0
#     }, fields=["name", "owner", "remainder"])

#     for call_list in call_lists:
#         if call_list['remainder']:
#             try:
#                 # Notification message
#                 message = f"Reminder for Call List: {call_list['name']}"

#                 # Send push notification using publish_realtime
#                 frappe.publish_realtime(
#                     event='call_list_reminder',
#                     message=message,
#                     user=call_list["owner"],
#                     after_commit=True
#                 )

#                 # Create a system notification using the Notification Log doctype
#                 notification_log = frappe.get_doc({
#                     "doctype": "Notification Log",
#                     "subject": "Call List Reminder",
#                     "email_content": message,
#                     "for_user": call_list["owner"],
#                     "document_type": "Call List",
#                     "document_name": call_list["name"]
#                 })
#                 notification_log.insert(ignore_permissions=True)
#                 # Mark the notification as sent
#                 frappe.db.set_value("Call List", call_list["name"], "remainder_notification_sent", 1)
                

#             except Exception as e:
#                 # Log the exception for troubleshooting
#                 frappe.log_error(frappe.get_traceback(), f"Failed to send notification for Call List: {call_list['name']}")
#     frappe.db.commit()

# send_reminder_notifications()








# import frappe
# from frappe.utils import now_datetime

# def send_reminder_notifications():
#     current_time = now_datetime()

#     # Fetch all call list entries where the reminder time is due and notification is not yet sent
#     call_lists = frappe.get_all("Call List", filters={
#         "remainder": ["<=", current_time],
#         "remainder_notification_sent": 0
#     }, fields=["name", "owner", "remainder"])

#     for call_list in call_lists:
#         if call_list['remainder']:
#             try:
#                 # Notification message
#                 message = f"Reminder for Call List: {call_list['name']}"

#                 # Send push notification using publish_realtime
#                 frappe.publish_realtime(
#                     event='call_list_reminder',
#                     message=message,
#                     user=call_list["owner"],
#                     after_commit=True
#                 )

#                 # Optionally display a pop-up notification for each reminder (not recommended in bulk operations)
#                 frappe.msgprint({
#                     "title": "Notification",
#                     "indicator": 'green',
#                     "message": message
#                 })

#                 # Create a system notification using the Notification Log doctype
#                 notification_log = frappe.get_doc({
#                     "doctype": "Notification Log",
#                     "subject": "Call List Reminder",
#                     "email_content": message,
#                     "for_user": call_list["owner"],
#                     "document_type": "Call List",
#                     "document_name": call_list["name"]
#                 })
#                 notification_log.insert(ignore_permissions=True)

#                 # Mark the notification as sent
#                 frappe.db.set_value("Call List", call_list["name"], "remainder_notification_sent", 1)

#             except Exception as e:
#                 # Log the exception for troubleshooting
#                 frappe.log_error(frappe.get_traceback(), f"Failed to send notification for Call List: {call_list['name']}")

#     frappe.db.commit()

# # Trigger the function
# send_reminder_notifications()





# import frappe
# from frappe.utils import now_datetime

# def send_reminder_notifications():
#     #frappe.log_error("Function 'send_reminder_notifications' started")

#     current_time = now_datetime()
#     #frappe.log_error(f"Current Time: {current_time}")

#     # Fetch all call list entries where the reminder time is due and notification is not yet sent
#     call_lists = frappe.get_all("Call List", filters={
#         "remainder": ["<=", current_time],
#         "remainder_notification_sent": 0
#     }, fields=["name", "owner", "remainder"])
    
#     #frappe.log_error(f"Total Call List entries found: {len(call_lists)}")

#     for call_list in call_lists:
#         frappe.log_error(f"Processing Call List entry: {call_list['name']}")
#         if call_list['remainder']:
#             try:
#                 # Notification message
#                 message = f"Reminder for Call List: {call_list['name']}"
#                 #frappe.log_error(f"Notification message: {message}")

#                 # Send push notification using publish_realtime
#                 frappe.publish_realtime(
#                     event='call_list_reminder',
#                     message=message,
#                     user=call_list["owner"],
#                     after_commit=True
#                 )
#                 frappe.log_error(f"Real-time notification sent for Call List: {call_list['name']}")

#                 frappe.publish_realtime(event='msgprint',message="Bob just created an issue...",user="Administrator")

#                 # Optionally display a pop-up notification for each reminder (not recommended in bulk operations)
#                 frappe.msgprint({
#                     "title": "Notification",
#                     "indicator": 'green',
#                     "message": message,
#                     "user":call_list["owner"]
#                 })
#                 frappe.log_error(f"user:{call_list['owner']}")
#                 frappe.log_error(f"Pop-up notification displayed for Call List: {call_list['name']}")

#                 # Create a system notification using the Notification Log doctype
#                 notification_log = frappe.get_doc({
#                     "doctype": "Notification Log",
#                     "subject": "Call List Reminder",
#                     "email_content": message,
#                     "for_user": call_list["owner"],
#                     "document_type": "Call List",
#                     "document_name": call_list["name"]
                    
#                 })
#                 notification_log.insert(ignore_permissions=True)
#                 frappe.log_error(f"Notification Log created for Call List: {call_list['name']}")

#                 # Mark the notification as sent
#                 frappe.db.set_value("Call List", call_list["name"], "remainder_notification_sent", 1)
#                 frappe.log_error(f"Notification marked as sent for Call List: {call_list['name']}")

#             except Exception as e:
#                 # Log the exception for troubleshooting
#                 error_message = f"Failed to send notification for Call List: {call_list['name']}"
#                 frappe.log_error(frappe.get_traceback(), error_message)
#                 frappe.log_error(f"Error: {error_message}")

#     frappe.db.commit()
#     #frappe.log_error("Database commit complete")

# # Trigger the function
# send_reminder_notifications()






##client script call list open
@frappe.whitelist()
def sent_reminder(docname):
    try:
        # Fetch the document and perform any logic
        doc = frappe.get_doc('Call List', docname)
        frappe.logger().info(f"Processing reminder for Call List: {docname}")
        # Returning a message to be shown in the popup
        return {"message": f"Reminder for Call List {doc.name} has been triggered."}
    
    except Exception as e:
        # In case of an error, log it and return a descriptive message
        frappe.log_error(message=str(e), title="Call List Reminder Error")
        frappe.logger().error(f"Error processing reminder for Call List {docname}: {str(e)}")
        return {"message": f"An error occurred: {str(e)}"}

## client script call list end 



# import frappe
# from frappe.utils import now_datetime

# def check_remainder_notifications():
#     # Fetch Call List documents where remainder time is due and notification not sent
#     now = now_datetime()
#     call_list_entries = frappe.get_all('Call List', filters={
#         'remainder': ['<=', now],
#         'remainder_notification_sent': 0
#     }, fields=['name', 'owner', 'remainder'])

#     for entry in call_list_entries:
#         # Send real-time notification to the user
#         frappe.publish_realtime(
#             event='call_list_reminder',
#             message={
#                 'docname': entry.name,
#                 'remainder': entry.remainder
#             },
#             user=entry.owner
#         )

#         # Mark the notification as sent
#         doc = frappe.get_doc('Call List', entry.name)
#         doc.remainder_notification_sent = 1
#         doc.save(ignore_permissions=True)

#         frappe.logger().info(f"Remainder notification sent for Call List: {entry.name}")









@frappe.whitelist()
def get_sales_person_details(sales_person):
    try:
        # Fetch total amount from quotations with status 'Order' for the selected sales person
        total_amount = frappe.db.get_all('Quotation',
            filters={
                'sales_person': sales_person,
                'status': 'Ordered'
            },
            fields=['sum(total']
        )
        total_amount = total_amount[0].get('sum(total)', 0) if total_amount else 0

        return {
            'total_amount': total_amount
        }

    except Exception as e:
        frappe.log_error(message=str(e), title="Sales Person Details Error")
        frappe.logger().error(f"Error fetching details for Sales Person {sales_person}: {str(e)}")
        return {
            'total_amount': 0
        }


@frappe.whitelist()
def get_sales_data(sales_person):
    query = """
        SELECT 
            c.name AS c_name,
            ci.item_name AS ci_item_name,
            ci.item_code AS ci_item_code,
            ci.qty AS ci_qty,
            ci.rate AS ci_rate,
            ci.amount AS ci_amount,
            ci.supplier AS ci_supplier,
            ci.supplier_item as ci_supplier_item,
            ci.supplier_rate as ci_supplier_rate,
            ci.supplier_amount AS ci_supplier_amount,
            ci.amount - ci.supplier_amount AS difference_amount,
            cis.sales_person AS cis_sales_person
        FROM 
            `tabCustomer Order Form` AS c 
        LEFT JOIN `tabCustomer Order Item` AS ci ON c.name = ci.parent
        LEFT JOIN `tabSales Team` AS cis ON c.name = cis.parent
        WHERE cis.sales_person = %s 
        ORDER BY c.name, ci.item_name, ci.rate, ci.qty ASC
    """
    data = frappe.db.sql(query, sales_person, as_dict=True)
    return data





