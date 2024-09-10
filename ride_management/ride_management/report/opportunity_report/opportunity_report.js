// Copyright (c) 2024, lakshman and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["opportunity report"] = {
	"filters": [
		{
			"fieldname":"name",
			"label":"Opportunity ID",
			"fieldtype":"Data",
			"width":100
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
			"fieldname":"from",
			"label":"From Date",
			"fieldtype":"Date",
			"width":100,
			"redg":1,
			"default":dateutil.year_start()
		},
		{
			"fieldname":"to",
			"label":"To Date",
			"fieldtype":"Date",
			"width":100,
			"redg":1,
			"default":dateutil.year_end()
		},
		{
			"fieldname":"item",
			"label":"Item",
			"fieldtype":"Data",
			"width":100
		}
	]
};
