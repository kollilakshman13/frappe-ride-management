
# apps/ride_management/ride_management/www/contact1.py


import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def handle_contact_form():
    try:
        frappe.log("Request method: " + frappe.local.request.method)
        frappe.log("Request headers: " + str(frappe.local.request.headers))

        if frappe.local.request.method != "POST":
            frappe.log_error("Invalid Request Method")
            frappe.throw(_("Invalid Request Method"), frappe.MethodNotAllowedError)

        data = frappe.local.form_dict
        frappe.log("Received form data: " + str(data))

        required_fields = ['name', 'email', 'phone_no', 'service_name', 'message']
        for field in required_fields:
            if not data.get(field):
                frappe.log_error(f"Missing field: {field}")
                frappe.throw(_(f"{field.capitalize()} is required"))

        name = data.get('name')
        email = data.get('email')
        phone_no = data.get('phone_no')
        service_name = data.get('service_name')
        message = data.get('message')
        subject = data.get('subject') or "New Contact Form Submission"

        message_body = f"""
                <p><b>Name:</b> {name}</p>
                <p><b>Email:</b> {email}</p>
                <p><b>Phone Number:</b> {phone_no}</p>
                <p><b>Service Name:</b> {service_name}</p>
                <p><b>Message:</b> {message}</p>
        """
        # #message_body = f""" 
        #     <div style="width:90%; margin: 0 auto;">
        #         <div style="width:100%;display: flex;align-items: center;">
        #             <!-- Logo Section -->
        #             <div style="width:20%;">
        #                 <img src="https://192.168.23.24:8000/image/64-Network-PNG-Logo 1.png" style="width: 100%; height:80px; object-fit:contain;">
        #             </div>
            
        #             <!-- Header Section -->
        #             <div style="width:80%; height:80px; background-color: #2C3E50;">
        #                 <!-- Replace with any header content if needed -->
        #             </div>
        #         </div>
            
        #         <!-- Main Content Section -->
        #         <div style="width:96%; display: flex; background-color: #1B4249; color:#ffffff; padding: 20px;">
        #             <div style="width:100%;">
        #                 <h2 style="font-size: 22px; margin-bottom: 10px;">Mobile Devices</h2>
        #                 <p><b style="color: #F0A500;">NAME:</b> Lakshman</p>
        #                 <p><b style="color: #F0A500;">Email:</b> kollilakshman07@gmail.com</p>
        #                 <p><b style="color: #F0A500;">Service Name:</b> Mobile Device Management (MDM)</p>
        #                 <p><b style="color: #F0A500;">Message:</b> Mobile</p>
        #             </div> 
        #         </div>
            
        #         <!-- Footer Section -->
        #         <div style="width:100%; height:80px; background-color:rgba(0, 0, 0, 0.97); text-align: center; color: #ffffff; display: flex; align-items: center; justify-content: center;">
        #             <p>&copy; 2024 64 Network Pvt Ltd. All rights reserved.</p>
        #         </div>
        #     </div>
        # """
         
        
        

        recipient_email = "kollilakshman13@gmail.com"
        # sender_email = frappe.session.user if frappe.session.user != "Guest" else "default-sender@example.com"
        # sender_email = frappe.session.user if frappe.session.user != "Guest" else email
        # Get the session user
        sender_email = frappe.session.user
        if sender_email == "Guest":
            email_account = frappe.get_value("Email Account", {"default_outgoing": 1}, "email_id")
            if email_account:
                sender_email = email_account
            else:
                sender_email = "your-default-sender-email@example.com"

        
        frappe.sendmail(recipients=[recipient_email], sender=sender_email, subject=subject, message=message_body)
        frappe.msgprint(_("Form submitted successfully! Email sent."))

        frappe.local.response.update({
            "status": "success",
            "message": "Form submitted successfully! Email sent."
        })
    except Exception as e:
        frappe.log_error(f"Failed to process form: {str(e)}")
        frappe.throw(_("There was an issue submitting the form. Please try again later."))
