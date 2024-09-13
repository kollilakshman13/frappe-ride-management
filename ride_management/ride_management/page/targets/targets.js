// frappe.pages['targets'].on_page_load = function(wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Target sales Person',
// 		single_column: true
// 	});

// }




/*frappe.pages['targets'].on_page_load = function(wrapper) {

    // Add Bootstrap for styling
    $('<link/>', {
        rel: 'stylesheet',
        href: 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        integrity: 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ775/z4Yr3t3Gsapm5lVrMm+4hlgO8aa4CD',
        crossorigin: 'anonymous'
    }).appendTo('head');

    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Target Sales Person Details',
        single_column: true
    });

    // Create a field to select Sales Person from the Sales Person doctype
    frappe.ui.form.make_control({
        parent: page.body,
        df: {
            fieldtype: 'Link',
            options: 'Sales Person',
            label: 'Select Sales Person',
            fieldname: 'sales_person',
            onchange: function() {
                var sales_person = this.get_value();
                if (sales_person) {
                    // Fetch target details of the selected sales person
                    frappe.call({
                        method: 'frappe.client.get',
                        args: {
                            doctype: 'Sales Person',
                            name: sales_person
                        },
                        callback: function(r) {
                            if (r.message) {
                                // Assuming r.message has target data like target_amount, reached_amount, etc.
                                var target_amount = r.message.target_amount || 1000000;
                                var reached_amount = r.message.reached_amount || 800000;
                                var remaining_amount = target_amount - reached_amount;

                                // Calculate grade based on percentage
                                var percentage = (reached_amount / target_amount) * 100;
                                var grade = calculate_grade(percentage);

                                // Display the sales person details
                                display_sales_person_details(sales_person, target_amount, reached_amount, remaining_amount, grade);
                            }
                        }
                    });
                }
            }
        },
        render_input: true
    }).refresh();

    // Function to display the sales person details in boxes
    function display_sales_person_details(name, target, reached, remaining, grade) {
        // Clear previous content
        $(page.body).find('.sales-person-details').remove();

        // Get color based on grade
        var gradeColor = get_grade_color(grade);

        // Create a container for the boxes
        var details_container = $(`
            <div class="sales-person-details" style="display: flex; justify-content: space-between; margin-top: 20px;">
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Target Amount</h5>
                    <p>${target}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Achieved Target</h5>
                    <p>${reached}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Remaining Target</h5>
                    <p>${remaining}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px; color: white; background-color: ${gradeColor};">
                    <h5>Grade</h5>
                    <p>${grade}</p>
                </div>
            </div>
        `);

        // Append the boxes to the page
        $(page.body).append(details_container);
    }

    // Function to calculate grade based on percentage
    function calculate_grade(percentage) {
        if (percentage >= 90) {
            return 'A+';
        } else if (percentage >= 80) {
            return 'A';
        } else if (percentage >= 70) {
            return 'B+';
        } else if (percentage >= 60) {
            return 'B';
        } else if (percentage >= 50) {
            return 'C+';
        } else {
            return 'C';
        }
    }

    // Function to get color based on grade
    function get_grade_color(grade) {
        switch (grade) {
            case 'A+':
                return '#B8860B';  // Glod
            case 'A':
				return '#ffc107';  // Yellow
            case 'B+':
                return '#007bff';  // Blue
            case 'B':
                return '#fd7e14';  // Orange
            case 'C+':
				return '#6c757d';  // Gray
            case 'C':
                return '#dc3545';  // Red
            default:
				return '#000000';  // Black	
        }
    }
}
*/


/*frappe.pages['targets'].on_page_load = function(wrapper) {

    // Add Bootstrap for styling
    $('<link/>', {
        rel: 'stylesheet',
        href: 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        integrity: 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ775/z4Yr3t3Gsapm5lVrMm+4hlgO8aa4CD',
        crossorigin: 'anonymous'
    }).appendTo('head');

    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Target Sales Person Details',
        single_column: true
    });

    // Create a field to select Sales Person from the Sales Person doctype
    frappe.ui.form.make_control({
        parent: page.body,
        df: {
            fieldtype: 'Link',
            options: 'Sales Person',
            label: 'Select Sales Person',
            fieldname: 'sales_person',
            onchange: function() {
                var sales_person = this.get_value();
				if (sales_person) {
					// Fetch target details of the selected sales person using the custom server-side method
					frappe.call({
						method: 'ride_management.tasks.get_sales_data',  // Use your actual method path
						args: {
							sales_person: sales_person
						},
						callback: function(r) {
							console.log(r.message);  // For debugging purposes
							if (r.message && r.message.length > 0) {
                                var total_target_amount = 0;
                                var total_reached_amount = 0;
                                
                                // Loop through each row in the result and calculate totals
                                r.message.forEach(function(row) {
                                    total_target_amount += row.ci_amount || 0;
                                    total_reached_amount += row.ci_supplier_amount || 0;
                                });
                
                                var remaining_amount = total_target_amount - total_reached_amount;
                                var percentage = (total_reached_amount / total_target_amount) * 100;
                                var grade = calculate_grade(percentage);
                
                                // Display the sales person details with the accumulated values
                                display_sales_person_details(sales_person, total_target_amount, total_reached_amount, remaining_amount, grade);
                            }
						}
					});
				}
					
            }
        },
        render_input: true
        
    }).refresh();

    

    // Function to display the sales person details in boxes
    function display_sales_person_details(name, target, reached, remaining, grade) {
        // Clear previous content
        $(page.body).find('.sales-person-details').remove();

        // Get color based on grade
        var gradeColor = get_grade_color(grade);

        // Create a container for the boxes
        var details_container = $(`
            <div class="sales-person-details" style="display: flex; justify-content: space-between; margin-top: 20px;">
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Target Amount</h5>
                    <p>${target}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Achieved Target</h5>
                    <p>${reached}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Remaining Target</h5>
                    <p>${remaining}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px; color: white; background-color: ${gradeColor};">
                    <h5>Grade</h5>
                    <p>${grade}</p>
                </div>
            </div>
            <div style="margin-top:20px;">
                <h2>Report </h2>
                <table style="width:100%;border:1px solid black;">
                    <tr style="border:1px solid black;">
                        <th style="border:1px solid black;">s.no</th>
                        <th style="border:1px solid black;">Cof ID </th>
                    </tr>
                    
                </table>
            </div>
        `);

        // Append the boxes to the page
        $(page.body).append(details_container);
    }

    // Function to calculate grade based on percentage
    function calculate_grade(percentage) {
        if (percentage >= 90) {
            return 'A+';
        } else if (percentage >= 80) {
            return 'A';
        } else if (percentage >= 70) {
            return 'B+';
        } else if (percentage >= 60) {
            return 'B';
        } else if (percentage >= 50) {
            return 'C+';
        } else {
            return 'C';
        }
    }

    // Function to get color based on grade
    function get_grade_color(grade) {
        switch (grade) {
            case 'A+':
                return '#B8860B';  // Gold
            case 'A':
                return '#ffc107';  // Yellow
            case 'B+':
                return '#007bff';  // Blue
            case 'B':
                return '#fd7e14';  // Orange
            case 'C+':
                return '#6c757d';  // Gray
            case 'C':
                return '#dc3545';  // Red
            default:
                return '#000000';  // Black
        }
    }
};*/








/*frappe.pages['targets'].on_page_load = function(wrapper) {

    // Add Bootstrap for styling
    $('<link/>', {
        rel: 'stylesheet',
        href: 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        integrity: 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ775/z4Yr3t3Gsapm5lVrMm+4hlgO8aa4CD',
        crossorigin: 'anonymous'
    }).appendTo('head');

    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Target Sales Person Details',
        single_column: true
    });

    // Create a field to select Sales Person from the Sales Person doctype
    frappe.ui.form.make_control({
        parent: page.body,
        df: {
            fieldtype: 'Link',
            options: 'Sales Person',
            label: 'Select Sales Person',
            fieldname: 'sales_person',
            onchange: function() {
                var sales_person = this.get_value();
                if (sales_person) {
                    // Fetch target details of the selected sales person using the custom server-side method
                    frappe.call({
                        method: 'ride_management.tasks.get_sales_data',  // Use your actual method path
                        args: {
                            sales_person: sales_person
                        },
                        callback: function(r) {
                            console.log(r.message);  // For debugging purposes
                            if (r.message && r.message.length > 0) {
                                var total_target_amount = 0;
                                var total_reached_amount = 0;
                                
                                // Loop through each row in the result and calculate totals
                                r.message.forEach(function(row) {
                                    total_target_amount += row.ci_amount || 0;
                                    total_reached_amount += row.ci_supplier_amount || 0;
                                });
                
                                var remaining_amount = total_target_amount - total_reached_amount;
                                var percentage = (total_reached_amount / total_target_amount) * 100;
                                var grade = calculate_grade(percentage);
                
                                // Display the sales person details with the accumulated values
                                display_sales_person_details(sales_person, total_target_amount, total_reached_amount, remaining_amount, grade);
                
                                // Display the report data in a table
                                display_sales_report(r.message);
                            }
                        }
                    });
                }
            }
        },
        render_input: true
    }).refresh();

    // Function to display the sales person details in boxes
    function display_sales_person_details(name, target, reached, remaining, grade) {
        // Clear previous content
        $(page.body).find('.sales-person-details').remove();

        // Get color based on grade
        var gradeColor = get_grade_color(grade);

        // Create a container for the boxes
        var details_container = $(`
            <div class="sales-person-details" style="display: flex; justify-content: space-between; margin-top: 20px;">
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Target Amount</h5>
                    <p>${target}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Achieved Target</h5>
                    <p>${reached}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Remaining Target</h5>
                    <p>${remaining}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px; color: white; background-color: ${gradeColor};">
                    <h5>Grade</h5>
                    <p>${grade}</p>
                </div>
            </div>
        `);

        // Append the boxes to the page
        $(page.body).append(details_container);
    }

    // Function to display the sales report data in a table
    function display_sales_report(data) {
        // Clear previous report
        $(page.body).find('.sales-report').remove();

        // Create the table structure
        var table = $(`
            <table class="sales-report table table-bordered" style="width:100%; margin-top:20px;border:1px solid black;">
                <thead>
                    <tr style="border:1px solid black;">
                        <th style="border:1px solid black;">S.No</th>
                        <th style="border:1px solid black;">Cof ID</th>
                        <th style="border:1px solid black;">Item Name</th>
                        <th style="border:1px solid black;">Qty</th>
                        <th style="border:1px solid black;">Rate</th>
                        <th style="border:1px solid black;">Amount</th>
                        <th style="border:1px solid black;">Supplier</th>
                        <th style="border:1px solid black;">Supplier Rate</th>
                        <th style="border:1px solid black;">Supplier Amount</th>
                        <th style="border:1px solid black;">Difference</th>
                        <th style="border:1px solid black;">Sales Person</th>
                    </tr>
                </thead>
                <tbody></tbody>
            </table>
        `);

        // Append the table to the page
        $(page.body).append(table);

        // Populate the table with data
        data.forEach(function(row, index) {
            var row_html = `
                <tr style="border:1px solid black;">
                    <td style="border:1px solid black;">${index + 1}</td>
                    <td style="border:1px solid black;">${row.c_name}</td>
                    <td style="border:1px solid black;">${row.ci_item_name}</td>
                    <td style="border:1px solid black;">${row.ci_qty}</td>
                    <td style="border:1px solid black;">${row.ci_rate}</td>
                    <td style="border:1px solid black;">${row.ci_amount}</td>
                    <td style="border:1px solid black;">${row.ci_supplier}</td>
                    <td style="border:1px solid black;">${row.ci_supplier_rate}</td>
                    <td style="border:1px solid black;">${row.ci_supplier_amount}</td>
                    <td style="border:1px solid black;">${row.difference_amount}</td>
                    <td style="border:1px solid black;">${row.cis_sales_person}</td>
                </tr>
            `;
            $(table).find('tbody').append(row_html);
        });
    }

    // Function to calculate grade based on percentage
    function calculate_grade(percentage) {
        if (percentage >= 90) {
            return 'A+';
        } else if (percentage >= 80) {
            return 'A';
        } else if (percentage >= 70) {
            return 'B+';
        } else if (percentage >= 60) {
            return 'B';
        } else if (percentage >= 50) {
            return 'C+';
        } else {
            return 'C';
        }
    }

    // Function to get color based on grade
    function get_grade_color(grade) {
        switch (grade) {
            case 'A+':
                return '#B8860B';  // Gold
            case 'A':
                return '#ffc107';  // Yellow
            case 'B+':
                return '#007bff';  // Blue
            case 'B':
                return '#fd7e14';  // Orange
            case 'C+':
                return '#6c757d';  // Gray
            case 'C':
                return '#dc3545';  // Red
            default:
                return '#000000';  // Black
        }
    }
};*/




/*frappe.pages['targets'].on_page_load = function(wrapper) {
    $('<link/>', {
        rel: 'stylesheet',
        href: 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        integrity: 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ775/z4Yr3t3Gsapm5lVrMm+4hlgO8aa4CD',
        crossorigin: 'anonymous'
    }).appendTo('head');

    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Target Sales Person Details',
        single_column: true
    });

    // Create a field to select Sales Person from the Sales Person doctype
    frappe.ui.form.make_control({
        parent: page.body,
        df: {
            fieldtype: 'Link',
            options: 'Sales Person',
            label: 'Select Sales Person',
            fieldname: 'sales_person',
            onchange: function() {
                var sales_person = this.get_value();
                if (sales_person) {
                    // Fetch target details of the selected sales person using the custom server-side method
                    frappe.call({
                        method: 'ride_management.tasks.get_sales_data',
                        args: {
                            sales_person: sales_person
                        },
                        callback: function(r) {
                            if (r.message && r.message.length > 0) {
                                var total_target_amount = 0;
                                var total_reached_amount = 0;
                                
                                // Loop through each row in the result and calculate totals
                                r.message.forEach(function(row) {
                                    total_target_amount += row.ci_amount || 0;
                                    total_reached_amount += row.ci_supplier_amount || 0;
                                });
                
                                var remaining_amount = total_target_amount - total_reached_amount;
                                var percentage = (total_reached_amount / total_target_amount) * 100;
                                var grade = calculate_grade(percentage);

                                // Display the sales person details
                                display_sales_person_details(sales_person, total_target_amount, total_reached_amount, remaining_amount, grade);

                                // Render the dynamic report model
                                render_report_model(sales_person);
                            }
                        }
                    });
                }
            }
        },
        render_input: true
    }).refresh();

    // Function to display the sales person details in boxes
    function display_sales_person_details(name, target, reached, remaining, grade) {
        $(page.body).find('.sales-person-details').remove();

        var gradeColor = get_grade_color(grade);
        var details_container = $(`
            <div class="sales-person-details" style="display: flex; justify-content: space-between; margin-top: 20px;">
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Target Amount</h5>
                    <p>${target}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Achieved Target</h5>
                    <p>${reached}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Remaining Target</h5>
                    <p>${remaining}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px; color: white; background-color: ${gradeColor};">
                    <h5>Grade</h5>
                    <p>${grade}</p>
                </div>
            </div>
        `);

        $(page.body).append(details_container);
    }

    // Function to render the report model
    function render_report_model(sales_person) {
        $(page.body).find('.report-container').remove();
        var report_container = $(`<div class="report-container" style="margin-top: 30px;"></div>`);
        $(page.body).append(report_container);

        frappe.query_reports["Customer order Form Report"] = {
            filters: [
                {
                    fieldname: "sales_person",
                    label: __("Sales Person"),
                    fieldtype: "Link",
                    options: "Sales Person",
                    default: sales_person
                }
            ]
        };

        // frappe.require("/assets/frappe/js/frappe/ui/reports/query_report.js", function() {
        //     frappe.query_report.load();
        // });

        frappe.require("ride_management/ride_management/report/customer_order_form_report/customer_order_form_report.js", function() {
            frappe.query_report.load();
        });
        
    }

    // Grade calculation and color functions (same as before)
    function calculate_grade(percentage) {
        if (percentage >= 90) return 'A+';
        if (percentage >= 80) return 'A';
        if (percentage >= 70) return 'B+';
        if (percentage >= 60) return 'B';
        if (percentage >= 50) return 'C+';
        return 'C';
    }

    function get_grade_color(grade) {
        switch (grade) {
            case 'A+': return '#B8860B';
            case 'A': return '#ffc107';
            case 'B+': return '#007bff';
            case 'B': return '#fd7e14';
            case 'C+': return '#6c757d';
            case 'C': return '#dc3545';
            default: return '#000000';
        }
    }
    // Function to render the report for the selected Sales Person on the same page
    function render_report_model(sales_person) {
        // Remove previous report container if it exists
        $(page.body).find('.report-container').remove();

        // Create a new container for the report
        var report_container = $('<div class="report-container" style="margin-top: 30px;"></div>');
        $(page.body).append(report_container);

        // Create iframe element for the report
        var report_iframe = $(`<iframe id="report-iframe" 
        src="/app/query-report/Customer%20Order%20Form%20Report?sales_person=${encodeURIComponent(sales_person)}&minimal=1"
        style="width: 100%; height: 800px; border: none;"></iframe>`);

        // Append the iframe to the report container
        report_container.append(report_iframe);

        // Wait for iframe to load to inject custom CSS to hide the navbar
        report_iframe.on('load', function() {
            var iframeContent = document.getElementById('report-iframe').contentWindow.document;

            // Inject CSS to hide the navbar inside the iframe
            var style = document.createElement('style');
            style.innerHTML = `
                .navbar { display: none !important; }
                .page-head { display: none !important; }
            `;
            
            iframeContent.head.appendChild(style);
        });
    }
};*/


frappe.pages['targets'].on_page_load = function(wrapper) {
    $('<link/>', {
        rel: 'stylesheet',
        href: 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        integrity: 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T',
        crossorigin: 'anonymous'
    }).appendTo('head');
    

    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Target Sales Person Details',
        single_column: true
    });

    // Create a field to select Sales Person from the Sales Person doctype
    frappe.ui.form.make_control({
        parent: page.body,
        df: {
            fieldtype: 'Link',
            options: 'Sales Person',
            label: 'Select Sales Person',
            fieldname: 'sales_person',
            
            onchange: function() {
                var sales_person = this.get_value();
                if (sales_person) {
                    // Fetch target details of the selected sales person using the custom server-side method
                    frappe.call({
                        method: 'ride_management.tasks.get_sales_data',
                        args: {
                            sales_person: sales_person
                        },
                        callback: function(r) {
                            if (r.message && r.message.length > 0) {
                                var total_target_amount = 0;
                                var total_reached_amount = 0;
                                
                                // Loop through each row in the result and calculate totals
                                r.message.forEach(function(row) {
                                    total_target_amount += row.ci_amount || 0;
                                    total_reached_amount += row.ci_supplier_amount || 0;
                                });
                
                                var remaining_amount = total_target_amount - total_reached_amount;
                                var percentage = (total_reached_amount / total_target_amount) * 100;
                                var grade = calculate_grade(percentage);

                                // Display the sales person details
                                display_sales_person_details(sales_person, total_target_amount, total_reached_amount, remaining_amount, grade);
                                
                                // Render the report for the selected Sales Person
                                render_report_model(sales_person);
                            }
                        }
                    });
                }
            }
        },
        render_input: true
    }).refresh();

    // Function to display the sales person details in boxes
    function display_sales_person_details(name, target, reached, remaining, grade) {
        $(page.body).find('.sales-person-details').remove();

        var gradeColor = get_grade_color(grade);
        var details_container = $(`
            <div class="sales-person-details" style="display: flex; justify-content: space-between; margin-top: 20px;">
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Target Amount</h5>
                    <p>${target}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Achieved Target</h5>
                    <p>${reached}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px;">
                    <h5>Remaining Target</h5>
                    <p>${remaining}</p>
                </div>
                <div class="box card text-center" style="width: 20%; padding: 10px; color: white; background-color: ${gradeColor};">
                    <h5>Grade</h5>
                    <p>${grade}</p>
                </div>
            </div>
        `);

        $(page.body).append(details_container);
    }

    // Grade calculation and color functions
    function calculate_grade(percentage) {
        if (percentage >= 90) return 'A+';
        if (percentage >= 80) return 'A';
        if (percentage >= 70) return 'B+';
        if (percentage >= 60) return 'B';
        if (percentage >= 50) return 'C+';
        return 'C';
    }

    function get_grade_color(grade) {
        switch (grade) {
            case 'A+': return '#B8860B';
            case 'A': return '#ffc107';
            case 'B+': return '#007bff';
            case 'B': return '#fd7e14';
            case 'C+': return '#6c757d';
            case 'C': return '#dc3545';
            default: return '#000000';
        }
    }

    // Function to render the report for the selected Sales Person on the same page
    function render_report_model(sales_person) {
        // Remove previous report container if it exists
        $(page.body).find('.report-container').remove();

        // Create a new container for the report
        var report_container = $('<div class="report-container" style="margin-top: 30px;"></div>');
        $(page.body).append(report_container);

        // Create iframe element for the report
        var report_iframe = $(`<iframe id="report-iframe" 
        src="/app/query-report/Customer%20Order%20Form%20Report?sales_person=${encodeURIComponent(sales_person)}&minimal=1"
        style="width: 100%; height: 800px; border: none;"></iframe>`);

        // Append the iframe to the report container
        report_container.append(report_iframe);

        // Wait for iframe to load to inject custom CSS to hide the navbar
        report_iframe.on('load', function() {
            var iframeContent = document.getElementById('report-iframe').contentWindow.document;

            // Inject CSS to hide the navbar inside the iframe
            var style = document.createElement('style');
            style.innerHTML = `
                .navbar { display: none !important; }
                .page-head { display: none !important; }
            `;
            
            iframeContent.head.appendChild(style);
        });
    }

};



