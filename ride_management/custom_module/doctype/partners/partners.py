# Copyright (c) 2024, lakshman and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
import frappe.defaults
from frappe import _, msgprint
from frappe.contacts.address_and_contact import (
	delete_contact_and_address,
	load_address_and_contact,
)
from frappe.desk.reportview import build_match_conditions, get_filters_cond
from frappe.model.mapper import get_mapped_doc
from frappe.model.naming import set_name_by_naming_series, set_name_from_naming_options
from frappe.model.rename_doc import update_linked_doctypes
from frappe.utils import cint, cstr, flt, get_formatted_email, today
from frappe.utils.user import get_users_with_role



class Partners(Document):	
	pass


@frappe.whitelist()
def get_partners_details(partner, posting_date=None, company=None):
        if not partner:
            frappe.throw(_("Partner is required"))

        partner_doc = frappe.get_doc("Partners", partner)

        if not partner_doc:
            frappe.throw(_("Partner {0} not found").format(partner))

        # Prepare the details to be returned
        partner_details = {
            "partner_name": partner_doc.partner_name,
            "customer_address": partner_doc.partner_primary_address,
            "partner_email": partner_doc.email_id,
            "contact_person":partner_doc.partner_primary_contact,
            "territory": partner_doc.territory,
            "price_list": partner_doc.default_price_list,
            "tax_id": partner_doc.tax_id
        }
            
        return partner_details


