// Copyright (c) 2024, lakshman and contributors
// For license information, please see license.txt
/* eslint-disable */

/*frappe.query_reports["Sales Order & Supplier Report"] = {
	"filters": [

		{
            "fieldname": "name",
            "label": "Sales Order ID",
            "fieldtype": "MultiSelectList",
            'get_data':function(){ return frappe.db.get_link_options('Sales Order')},
            "width": 100
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
            "fieldtype": "MultiSelectList",
            'get_data':function(){ return frappe.db.get_link_options('Item')},
            "width": 100
        },
        {
            "fieldname": "item_group",
            "label": "Item Groups",
            "fieldtype": "MultiSelectList",
            'get_data':function(){ return frappe.db.get_link_options('Item Group')},
            "width": 100
        },
        {
            "fieldname": "brand",
            "label": "Brand",
            "fieldtype": "MultiSelectList",
			'get_data':function(){ return frappe.db.get_link_options('Brand')},
            "width": 100
        }
	],
    
    onload: function(report) {
        // Initialize report settings if not already initialized
        if (!report.report_settings) {
            report.report_settings = {};
        }

        // Set default columns initially
        report.report_settings.columns = get_columns();

        report.page.add_inner_button(__('Select Fields'), function() {
            show_field_selection_dialog(report);
        });
    }
};


function show_field_selection_dialog(report) {
    const dialog = new frappe.ui.Dialog({
        title: __('Select Fields to Display'),
        fields: [
            {
                fieldname: 'fields_to_display',
                label: 'List View',
                fieldtype: 'MultiCheck',
                options: [
                    {label: 'Sales Order ID', value: 'so_name'},
                    {label: 'Supplier ID', value: 'sq_name'},
                    {label: 'Customer', value: 'so_customer'},
                    {label: 'Supplier Name', value: 'sq_supplier'},
                    {label: 'Date', value: 'so_transaction_date'},
                    {label: 'Item Name', value: 'soi_item_code'},
                    {label: 'Sales Qty', value: 'soi_qty'},
                    {label: 'Sales Rate', value: 'soi_rate'},
                    {label: 'Sales Amount', value: 'soi_amount'},
                    {label: 'Purchase Rate', value: 'supplier_quotation_item_rate'},
                    {label: 'Purchase Amount', value: 'supplier_quotation_item_amount'},
                    {label: 'Difference Amount', value: 'difference_amount'},
                    {label: 'Sales Person', value: 'cis_sales_person'}
                ]
            }
        ],
        primary_action_label: 'Apply',
        primary_action(values) {
            apply_field_selection(report, values.fields_to_display);
            dialog.hide();
        }
    });

    dialog.show();
}


function apply_field_selection(report, selected_fields) {
    console.log("Selected Fields:", selected_fields);  // Debugging

    // Get all available columns
    const all_columns = get_columns();

    // Filter the columns based on selected fields
    const filtered_columns = all_columns.filter(column => selected_fields.includes(column.fieldname));

    console.log("Filtered Columns:", filtered_columns);  // Debugging

    // Set the filtered columns in the report's report_settings
    if (filtered_columns.length > 0) {
        // Set the filtered columns
        report.report_settings.columns = filtered_columns;
    } else {
        // If no fields were selected, use the default columns
        report.report_settings.columns = all_columns;
    }

    // Re-run the report with the updated columns
    report.refresh();
}*/




/*function get_columns() {
    return [
        {"label": "Sales Order ID", "fieldname": "so_name", "fieldtype": "Link", "options": "Sales Order", "width": 200},
        {"label": "Supplier ID", "fieldname": "sq_name", "fieldtype": "Link", "options": "Supplier Quotation", "width": 200},
        {"label": "Customer", "fieldname": "so_customer", "fieldtype": "Link", "options": "Customer", "width": 200},
        {"label": "Supplier Name", "fieldname": "sq_supplier", "fieldtype": "Link", "options": "Supplier", "width": 200},
        {"label": "Date", "fieldname": "so_transaction_date", "fieldtype": "Date", "width": 100},
        {"label": "Item Name", "fieldname": "soi_item_code", "fieldtype": "Link", "options": "Item", "width": 200},
        {"label": "Sales Qty", "fieldname": "soi_qty", "fieldtype": "Float", "width": 100},
        {"label": "Sales Rate", "fieldname": "soi_rate", "fieldtype": "Currency", "width": 150},
        {"label": "Sales Amount", "fieldname": "soi_amount", "fieldtype": "Currency", "width": 150},
        {"label": "Purchase Rate", "fieldname": "supplier_quotation_item_rate", "fieldtype": "Currency", "width": 150},
        {"label": "Purchase Amount", "fieldname": "supplier_quotation_item_amount", "fieldtype": "Currency", "width": 150},
        {"label": "Difference Amount", "fieldname": "difference_amount", "fieldtype": "Currency", "width": 150},
        {"label": "Sales Person", "fieldname": "cis_sales_person", "fieldtype": "Link", "options": "Sales Person", "width": 150}
    ];
}*/


frappe.query_reports["Sales Order & Supplier Report"] = {
    "filters": [
        // Your existing filters...
        {
            "fieldname": "name",
            "label": "Sales Order ID",
            "fieldtype": "MultiSelectList",
            'get_data':function(){ return frappe.db.get_link_options('Sales Order')},
            "width": 100
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
            "fieldtype": "MultiSelectList",
            'get_data':function(){ return frappe.db.get_link_options('Item')},
            "width": 100
        },
        {
            "fieldname": "item_group",
            "label": "Item Groups",
            "fieldtype": "MultiSelectList",
            'get_data':function(){ return frappe.db.get_link_options('Item Group')},
            "width": 100
        },
        {
            "fieldname": "brand",
            "label": "Brand",
            "fieldtype": "MultiSelectList",
			'get_data':function(){ return frappe.db.get_link_options('Brand')},
            "width": 100
        }
    ],
    
    onload: function(report) {
        if (!report.report_settings) {
            report.report_settings = {};
        }
        report.report_settings.columns = get_columns();

        report.page.add_inner_button(__('Select Fields'), function() {
            show_field_selection_dialog(report);
        });
    }
};

function show_field_selection_dialog(report) {
    const dialog = new frappe.ui.Dialog({
        title: __('Select Fields to Display'),
        fields: [
            {
                fieldname: 'fields_to_display',
                label: 'List View',
                fieldtype: 'MultiCheck',
                options: [
                    {label: 'Sales Order ID', value: 'so_name'},
                    {label: 'Supplier ID', value: 'sq_name'},
                    {label: 'Customer', value: 'so_customer'},
                    {label: 'Supplier Name', value: 'sq_supplier'},
                    {label: 'Date', value: 'so_transaction_date'},
                    {label: 'Item Name', value: 'soi_item_code'},
                    {label: 'Sales Qty', value: 'soi_qty'},
                    {label: 'Sales Rate', value: 'soi_rate'},
                    {label: 'Sales Amount', value: 'soi_amount'},
                    {label: 'Purchase Rate', value: 'supplier_quotation_item_rate'},
                    {label: 'Purchase Amount', value: 'supplier_quotation_item_amount'},
                    {label: 'Difference Amount', value: 'difference_amount'},
                    {label: 'Sales Person', value: 'cis_sales_person'}
                ]
            }
        ],
        primary_action_label: 'Apply',
        primary_action(values) {
            apply_field_selection(report, values.fields_to_display);
            dialog.hide();
        }
    });

    dialog.show();
}

function apply_field_selection(report, selected_fields) {
    console.log("Selected Fields:", selected_fields);

    if (selected_fields.length > 0) {
        report.set_filter_value('selected_columns', selected_fields);
    }

    report.refresh();
}













