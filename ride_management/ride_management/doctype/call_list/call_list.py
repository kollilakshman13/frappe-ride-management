# Copyright (c) 2024, lakshman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime
class CallList(Document):
    pass


	# def check_remainder_and_notify():
	# 	current_time = now_datetime()

	# 	call_list = frappe.get_all('Call List', 
	# 		filters={'remainder': ['<=', current_time], 
	# 			'remainder': ['!=', None]},
	# 		fields=['name', 'remainder', 'owner'])

	# 	for call in call_list:
	# 		# Create the notification
	# 		notification_message = f"Reminder: You have a call scheduled at {call['remainder']}."
			
	# 		# Send the notification
	# 		frappe.publish_realtime(
	# 			event='msgprint',
	# 			message=notification_message,
	# 			user=call['owner']
	# 		)

	# 		# Optionally, you can also mark the remainder as notified or clear it to avoid duplicate notifications
	# 		frappe.db.set_value('Call List', call['name'], 'remainder', None)


# from frappe.utils import now_datetime

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


# custom_app/custom_app/call_list_notification.py

# import frappe
# from frappe.utils import now_datetime

# def send_remainder_notifications():
#     current_time = now_datetime()
    
#     # Fetch all call list entries where the remainder time is due and notification is not yet sent
#     call_lists = frappe.get_all("Call List", filters={
#         "remainder": ["<=", current_time],
#         "remainder_notification_sent": 0
#     }, fields=["name", "owner", "remainder"])

#     for call_list in call_lists:
#         try:
#             # Send notification to the owner of the call list
#             message = f"Reminder for Call List: {call_list['name']}"

#             frappe.sendmail(
#                 recipients=call_list["owner"],
#                 subject="Call List Reminder",
#                 message=message
#             )

#             # # Send in-app system notification
#             # frappe.utils.notify(
#             #     recipients=call_list["owner"],
#             #     message=message,
#             #     title="Call List Reminder",
#             #     document_type="Call List",
#             #     document_name=call_list["name"]
#             # )
            
#             # Mark the notification as sent
#             frappe.db.set_value("Call List", call_list["name"], "remainder_notification_sent", 1)
#             frappe.db.commit()

#         except Exception as e:
#             # Log the exception for troubleshooting
#             frappe.log_error(frappe.get_traceback(), f"Failed to send notification for Call List: {call_list['name']}")

# send_remainder_notifications()

# import frappe
# from frappe.utils import now_datetime

# def send_remainder_notifications():
#     current_time = now_datetime()
    
#     # Fetch all call list entries where the reminder time is due and notification is not yet sent
#     call_lists = frappe.get_all("Call List", filters={
#         "remainder": ["<=", current_time],
#         "remainder_notification_sent": 0
#     }, fields=["name", "owner", "remainder"])

#     for call_list in call_lists:
#         try:
#             # Send email notification to the owner of the call list
#             message = f"Reminder for Call List: {call_list['name']}"

#             frappe.sendmail(
#                 recipients=call_list["owner"],
#                 subject="Call List Reminder",
#                 message=message
#             )

#             # Create a system notification using the Notification Log doctype
#             notification_log = frappe.get_doc({
#                 "doctype": "Notification Log",
#                 "subject": "Call List Reminder",
#                 "email_content": message,
#                 "for_user": call_list["owner"],
#                 "document_type": "Call List",
#                 "document_name": call_list["name"]
#             })
#             notification_log.insert(ignore_permissions=True)

#             # # Send push notification using publish_realtime
#             frappe.publish_realtime(
#                 event='call_list_reminder',
#                 message=message,
#                 user=call_list["owner"],
#                 after_commit=True
#             )
            
#             # Mark the notification as sent
#             frappe.db.set_value("Call List", call_list["name"], "remainder_notification_sent", 1)
#             frappe.db.commit()

#         except Exception as e:
#             # Log the exception for troubleshooting
#             frappe.log_error(frappe.get_traceback(), f"Failed to send notification for Call List: {call_list['name']}")

# send_remainder_notifications()





# call_list.py
# import frappe
# from frappe.utils import now_datetime

# def send_remainder_notifications():
#     current_time = now_datetime()

#     # Fetch all call list entries where the reminder time is due and notification is not yet sent
#     call_lists = frappe.get_all("Call List", filters={
#         "remainder": ["<=", current_time],
#         "remainder_notification_sent": 0
#     }, fields=["name", "owner", "remainder"])

#     for call_list in call_lists:
#         try:
#             # Send email notification to the owner of the call list
#             message = f"Reminder for Call List: {call_list['name']}"

#             frappe.sendmail(
#                 recipients=call_list["owner"],
#                 subject="Call List Reminder",
#                 message=message
#             )

#             # Create a system notification using the Notification Log doctype
#             notification_log = frappe.get_doc({
#                 "doctype": "Notification Log",
#                 "subject": "Call List Reminder",
#                 "email_content": message,
#                 "for_user": call_list["owner"],
#                 "document_type": "Call List",
#                 "document_name": call_list["name"]
#             })
#             notification_log.insert(ignore_permissions=True)

#             # Send push notification using publish_realtime
#             frappe.publish_realtime(
#                 event='call_list_reminder',
#                 message=message,
#                 user=call_list["owner"],
#                 after_commit=True
#             )
            
#             # Mark the notification as sent
#             frappe.db.set_value("Call List", call_list["name"], "remainder_notification_sent", 1)

#         except Exception as e:
#             # Log the exception for troubleshooting
#             frappe.log_error(frappe.get_traceback(), f"Failed to send notification for Call List: {call_list['name']}")
    
#     # Commit after all operations are done
#     frappe.db.commit()


frappe.publish_realtime(event='msgprint',message="Bob just created an issue...",user="Administrator")





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






