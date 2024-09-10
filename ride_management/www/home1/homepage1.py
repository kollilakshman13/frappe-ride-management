import frappe

def get_context(context):
    context.details=frappe.get_doc("solutions")
    return context 
