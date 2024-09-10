// Copyright (c) 2024, lakshman and contributors
// For license information, please see license.txt
/* eslint-disable */

/*frappe.query_reports["COF Report"] = {
	"filters": [
		
	]
};*/

frappe.query_reports["COF Report"] = {
    "filters": [
        {
            "fieldname": "name",
            "label": "COF ID",
            "fieldtype": "Link",
			"options":"Customer Order Form",
            "width": 100
        },
		{
			"fieldname":"customer_name",
			"label":"Customer",
			"fieldtype":"Link",
			"options":"Customer",
			"width":100,
			"redg":0
		},
        {
            "fieldname": "supplier_name",
            "label": "Supplier",
            "fieldtype": "Link",
            "options":"Supplier",
            "width": 100,
            "redg": 0
        },
        {
            "fieldname": "from",
            "label": "From Date",
            "fieldtype": "Date",
            "width": 100,
            "redg": 1,
            "default": dateutil.year_start()
        },
        {
            "fieldname": "to",
            "label": "To Date",
            "fieldtype": "Date",
            "width": 100,
            "redg": 1,
            "default": dateutil.year_end()
        },
        {
            "fieldname": "item",
            "label": "Item",
            "fieldtype": "Link",
			"options":"Item",
            "width": 100
        },
		{
            "fieldname": "brand",
            "label": "Brand",
            "fieldtype": "Link",
			"options":"Brand",
            "width": 100
        },
		{
			"fieldname": "company",
            "label": "Company Name",
            "fieldtype": "Link",
			"options":"Company",
            "width": 100
		},
		{
			"fieldname": "sales",
            "label": "Sales Person",
            "fieldtype": "Link",
			"options":"Sales Person",
            "width": 100
		}
    ]
}


