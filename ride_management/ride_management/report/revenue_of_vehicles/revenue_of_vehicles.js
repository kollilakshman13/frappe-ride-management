// Copyright (c) 2024, lakshman and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["revenue of vehicles"] = {
	"filters": [
        {
			"fieldname":"Vehicle",
			"label":"Vehicles",
			"fieldtype":"Link",
			"options":"Vehicles",
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
            "fieldname":"total_amount",
			"label":"Total Amount",
			"fieldtype":"Currency",
			"width":100,
			"redg":1
		},
		{
			"fieldname":"status",
			"label":"Status",
			"fieldtype":"Select",
			"default":'',
			"options":[' ','New','Accept','Rejected'],
			"width":100,
			"redg":0
		}

	]
};
