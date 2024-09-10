// Copyright (c) 2023, lakshman and contributors
// For license information, please see license.txt

frappe.ui.form.on('driverss', {
	// refresh: function(frm) {
     map:function(frm) {
		console.log(JSON.parse(frm.doc.map));
	 }
	// }
});
