// frappe.pages['today-activity'].on_page_load = function(wrapper) {

// 	$('<link/>', {
//         rel: 'stylesheet',
//         href: 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
//         integrity: 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ775/z4Yr3t3Gsapm5lVrMm+4hlgO8aa4CD',
//         crossorigin: 'anonymous'
//     }).appendTo('head');

// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Today Activities',
// 		single_column: true
// 	});
// }



frappe.pages['today-activity'].on_page_load = function(wrapper) {
    // Load Bootstrap CSS
    $('<link/>', {
        rel: 'stylesheet',
        href: 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        integrity: 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ775/z4Yr3t3Gsapm5lVrMm+4hlgO8aa4CD',
        crossorigin: 'anonymous'
    }).appendTo('head');

    // Create the page
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Today Activities',
        single_column: true
    });

    // Get today's date and calculate the previous day's date
    let today = frappe.datetime.get_today();
    let tomorrow = frappe.datetime.add_days(today, 1);

    // Fetch opportunities with expected_closing date as yesterday
    frappe.call({
        method: 'frappe.client.get_list',
        args: {
            doctype: 'Opportunity',
            fields: ['name', 'title', 'expected_closing', 'status','converted_by'],
            filters: [
                ['expected_closing', 'in', [today, tomorrow]]
			]
        },
        callback: function(r) {
            if (r.message && r.message.length > 0) {
                // Display the list of opportunities
                let $wrapper = $(wrapper).find('.page-content');
                let $table = $('<table class="table table-striped"><thead><tr><th>Opportunity</th><th>Title</th><th>Expected Closing</th><th>Status</th><th>Converted By</th></tr></thead><tbody></tbody></table>');
                
                r.message.forEach(function(opportunity) {
                    $table.find('tbody').append(`
                        <tr>
                            
							<td><a href="form/Opportunity/${opportunity.name}" class="btn-link">${opportunity.name}</a></td>

                            <td>${opportunity.title}</td>
                            <td>${opportunity.expected_closing}</td>
                            <td>${opportunity.status}</td>
							<td>${opportunity.converted_by}</td>
                        </tr>
                    `);
                });

                $wrapper.append($table);
            } else {
                // If no opportunities are found
                $(wrapper).find('.page-content').append('<p>No opportunities with expected closing date of tomorrow or today found.</p>');
            }
        }
    });
};
