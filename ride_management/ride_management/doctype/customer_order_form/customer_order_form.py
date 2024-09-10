# Copyright (c) 2024, lakshman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CustomerOrderForm(Document):
	pass

#import frappe
#from frappe.model.document import Document

#class CustomerOrderForm(Document):
#    def fetch_supplier_quotation_items(self):
#        for item in self.items:
#            # Fetch values from the database based on some condition (here, 'opportunity' field)
#            supplier = frappe.db.get_value('Supplier Quotation', {'name': self.opportunity}, ['supplier', 'name'])
#            suppliers = frappe.db.get_all('Supplier Quotation Item', filters={'parent': self.opportunity}, fields=['item_name', 'item_code', 'qty', #'rate', 'amount'])
#            # Set the 'supplier' field of the current item
#            if supplier:
#                item.supplier = supplier[0]  # Assign the first value ('supplier')
#
#            # Iterate over the fetched items and set the fields of the current item
#            for sup in suppliers:
#                item.item_name = sup['item_name']
#                # item.item_code = sup['item_code']  # Uncomment if needed 
#                item.supplier_qty = sup['qty']
#                item.supplier_rate = sup['rate']
#                item.supplier_amount = sup['amount']

        # Save the changes
#        self.save()


#order_form = frappe.get_doc("Customer Order Form", "Document")
#order_form.fetch_supplier_quotation_items()

# my_app/my_app/doctype/customer_order/customer_order.py


