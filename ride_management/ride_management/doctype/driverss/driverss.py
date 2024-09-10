# Copyright (c) 2023, lakshman and contributors
# For license information, please see license.txt

import frappe
from frappe.model import document
from frappe.website.website_generator import WebsiteGenerator

class driverss(WebsiteGenerator):
	def before_save(self):
		self.full_name=self.first_name+" "+self.last_name
	def before_insert(self):
		self.car="TATA"	




