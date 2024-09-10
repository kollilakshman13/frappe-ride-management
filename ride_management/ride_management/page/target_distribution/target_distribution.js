// frappe.pages['target-distribution'].on_page_load = function(wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Target List ',
// 		single_column: true
// 	});
	
// }

/*frappe.pages['target-distribution'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Target List',
		single_column: true
	});

	// Create a div for the sales team container
	let sales_team_box = $('<div class="box">Sales Team</div>').appendTo(page.body);

	// Create a nested div for the amount and add it inside the sales team box
	let amount_box = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box);

	let sales_team_box1 = $('<div class="box">Sales Team1</div>').appendTo(sales_team_box);
	let amount_box1 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box1);

	let sales_team_box1_1 = $('<div class="box">Sales leader1.1</div>').appendTo(sales_team_box1);
	let amount_box1_1 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box1_1);
	let sales_team_box2_1 = $('<div class="box">Sales leader1.2</div>').appendTo(sales_team_box1);
	let amount_box2_1 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box2_1);
	let sales_team_box3_1 = $('<div class="box">Sales leader1.3</div>').appendTo(sales_team_box1);
	let amount_box3_1 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box3_1);

	let sales_team_box1_11 = $('<div class="box">Sales person1</div>').appendTo(sales_team_box1_1);
	let amount_box1_11 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box1_11);
	let sales_team_box1_12 = $('<div class="box">Sales person2</div>').appendTo(sales_team_box1_1);
	let amount_box1_12 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box1_12);
	let sales_team_box1_13 = $('<div class="box">Sales person3</div>').appendTo(sales_team_box1_1);
	let amount_box1_13 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box1_13);

	let sales_team_box2_11 = $('<div class="box">Sales person1</div>').appendTo(sales_team_box2_1);
	let amount_box2_11 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box2_11);
	let sales_team_box2_12 = $('<div class="box">Sales person2</div>').appendTo(sales_team_box2_1);
	let amount_box2_12 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box2_12);
	let sales_team_box2_13 = $('<div class="box">Sales person3</div>').appendTo(sales_team_box2_1);
	let amount_box2_13 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box2_13);

	let sales_team_box3_11 = $('<div class="box">Sales person1</div>').appendTo(sales_team_box3_1);
	let amount_box3_11 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box3_11);
	let sales_team_box3_12 = $('<div class="box">Sales person2</div>').appendTo(sales_team_box3_1);
	let amount_box3_12 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box3_12);
	let sales_team_box3_13 = $('<div class="box">Sales person3</div>').appendTo(sales_team_box3_1);
	let amount_box3_13 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box3_13);

}*/





/*frappe.pages['target-distribution'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Target List',
		single_column: true
	});

	// Include the CSS file
	frappe.require("/assets/ride_management/css/tree.css");

	// Rest of your JavaScript code...
	// Create a div for the sales team container
	let sales_team_box = $('<div class="box">Sales Team</div>').appendTo(page.body);

	// Create a nested div for the amount and add it inside the sales team box
	let amount_box = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box);

	// Sales Team 1
	let sales_team_box1 = $('<div class="box">Sales Team1</div>').appendTo(sales_team_box);
	let amount_box1 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box1);

	// Sales Leader 1.1
	let sales_team_box1_1 = $('<div class="box">Sales leader1.1</div>').appendTo(sales_team_box1);
	let amount_box1_1 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box1_1);

	// Sales Leader 1.2
	let sales_team_box2_1 = $('<div class="box">Sales leader1.2</div>').appendTo(sales_team_box1);
	let amount_box2_1 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box2_1);

	// Sales Leader 1.3
	let sales_team_box3_1 = $('<div class="box">Sales leader1.3</div>').appendTo(sales_team_box1);
	let amount_box3_1 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box3_1);

	// Sales Person 1.1.x
	let sales_team_box1_11 = $('<div class="box">Sales person1</div>').appendTo(sales_team_box1_1);
	let amount_box1_11 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box1_11);

	let sales_team_box1_12 = $('<div class="box">Sales person2</div>').appendTo(sales_team_box1_1);
	let amount_box1_12 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box1_12);

	let sales_team_box1_13 = $('<div class="box">Sales person3</div>').appendTo(sales_team_box1_1);
	let amount_box1_13 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box1_13);

	// Sales Person 1.2.x
	let sales_team_box2_11 = $('<div class="box">Sales person1</div>').appendTo(sales_team_box2_1);
	let amount_box2_11 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box2_11);

	let sales_team_box2_12 = $('<div class="box">Sales person2</div>').appendTo(sales_team_box2_1);
	let amount_box2_12 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box2_12);

	let sales_team_box2_13 = $('<div class="box">Sales person3</div>').appendTo(sales_team_box2_1);
	let amount_box2_13 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box2_13);

	// Sales Person 1.3.x
	let sales_team_box3_11 = $('<div class="box">Sales person1</div>').appendTo(sales_team_box3_1);
	let amount_box3_11 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box3_11);

	let sales_team_box3_12 = $('<div class="box">Sales person2</div>').appendTo(sales_team_box3_1);
	let amount_box3_12 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box3_12);

	let sales_team_box3_13 = $('<div class="box">Sales person3</div>').appendTo(sales_team_box3_1);
	let amount_box3_13 = $('<div class="box" style="border:1px solid black;width:300px;">Amount</div>').appendTo(sales_team_box3_13);

}*/






/*frappe.pages['target-distribution'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Target List',
        single_column: true
    });

    // Include the CSS file
    frappe.require("/assets/ride_management/css/tree.css");

    let treeContainer = $('<div class="tree-container"></div>').appendTo(page.body);

    // Create the root node
    let rootBox = $('<div class="box root">Sales Team</div>').appendTo(treeContainer);
    $('<div class="box amount-box">Amount</div>').appendTo(rootBox);

    // First level nodes (Sales Team1)
    let level1 = $('<div class="box">Sales Team1</div>').appendTo(treeContainer);
    $('<div class="connector vertical"></div>').appendTo(level1);
    $('<div class="connector horizontal left"></div>').appendTo(level1);
    $('<div class="box amount-box">Amount</div>').appendTo(level1);

    // Second level nodes (Sales leaders)
    let leaders = ["Sales leader1.1", "Sales leader1.2", "Sales leader1.3"];
    leaders.forEach((leader, index) => {
        let leaderBox = $(`<div class="box orange">${leader}</div>`).appendTo(treeContainer);
        $('<div class="connector vertical"></div>').appendTo(leaderBox);
        $('<div class="connector horizontal left"></div>').appendTo(leaderBox);
        $('<div class="box amount-box">Amount</div>').appendTo(leaderBox);

        // Third level nodes (Sales persons)
        let persons = [`Sales person${index+1}.1`, `Sales person${index+1}.2`, `Sales person${index+1}.3`];
        persons.forEach(person => {
            let personBox = $(`<div class="box">${person}</div>`).appendTo(treeContainer);
            $('<div class="connector vertical"></div>').appendTo(personBox);
            $('<div class="connector horizontal right"></div>').appendTo(personBox);
            $('<div class="box amount-box">Amount</div>').appendTo(personBox);
        });
    });
}*/










/*frappe.pages['target-distribution'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Target List',
        single_column: true
    });

    // Include the CSS file
    frappe.require("/assets/ride_management/css/tree.css");

    // Create the root node
    let treeContainer = $('<div class="tree-container"></div>').appendTo(page.body);
    let rootBox = $('<div class="box root">Sales Team</div>').appendTo(treeContainer);
    $('<div class="box amount-box">Amount</div>').appendTo(rootBox);

    // First level node (Sales Team1)
    let level1Container = $('<div class="tree-container"></div>').appendTo(rootBox);
    let level1Box = $('<div class="box">Sales Team1</div>').appendTo(level1Container);
    $('<div class="box amount-box">Amount</div>').appendTo(level1Box);

    // Second level nodes (Sales leaders)
    let leadersContainer = $('<div class="tree-container"></div>').appendTo(level1Box);
    let leaders = ["Sales leader1.1", "Sales leader1.2", "Sales leader1.3"];
    leaders.forEach((leader, index) => {
        let leaderBox = $(`<div class="box orange">${leader}</div>`).appendTo(leadersContainer);
        $('<div class="box amount-box">Amount</div>').appendTo(leaderBox);

        // Third level nodes (Sales persons)
        let personsContainer = $('<div class="tree-container"></div>').appendTo(leaderBox);
        let persons = [`Sales person${index+1}.1`, `Sales person${index+1}.2`, `Sales person${index+1}.3`];
        persons.forEach(person => {
            let personBox = $(`<div class="box">${person}</div>`).appendTo(personsContainer);
            $('<div class="box amount-box">Amount</div>').appendTo(personBox);
        });
    });
}*/









/***frappe.pages['target-distribution'].on_page_load = function(wrapper) {

	// Include Bootstrap CSS
    $('<link/>', {
        rel: 'stylesheet',
        href: 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        integrity: 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ775/z4Yr3t3Gsapm5lVrMm+4hlgO8aa4CD',
        crossorigin: 'anonymous'
    }).appendTo('head');

    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Target List',
        single_column: true
    });

    // Include the CSS file
    frappe.require("/assets/ride_management/css/tree.css");

    // Create the root node
    let treeContainer = $('<div class="tree"></div>').appendTo(page.body);
    let rootBox = $('<div class="node root">Sales Team</div>').appendTo(treeContainer);
	$('<div class="box amount-box" style="border:1px solid black;padding:5px;margin-bottom:5px;">Amount</div>').appendTo(rootBox);
    // First level nodes (Sales Team1)
    let level1Container = $('<div class="children"></div>').appendTo(rootBox);
    let level1Box = $('<div class="node mt-2">Sales Team1</div>').appendTo(level1Container);
	$('<div class="box amount-box" style="border:1px solid black;padding:5px;margin-bottom:5px;">Amount</div>').appendTo(level1Box);

    // Second level nodes (Sales leaders)
    let leadersContainer = $('<div class="children mt-2 mb-3"></div>').appendTo(level1Box);
    let leaders = ["Sales leader1.1", "Sales leader1.2", "Sales leader1.3"];
    leaders.forEach((leader, index) => {
        let leaderBox = $(`<div class="node mt-3 mb-3" style="margin-bottom:5px;">${leader}</div>`).appendTo(leadersContainer);
		$('<div class="box amount-box" style="border:1px solid black;padding:5px;margin-bottom:5px">Amount</div>').appendTo(leaderBox);
        // Third level nodes (Sales persons)
        let personsContainer = $('<div class="children mb-2"></div>').appendTo(leaderBox);
        let persons = [`Sales person${index+1}.1`, `Sales person${index+1}.2`, `Sales person${index+1}.3`];
        persons.forEach(person => {
            let personBox = $(`<div class="node">${person}</div>`).appendTo(personsContainer);
			$('<div class="box amount-box" style="border:1px solid black;padding:5px;margin-bottom:5px">Amount</div>').appendTo(personBox);
        });
    });
}***/







frappe.pages['target-distribution'].on_page_load = function(wrapper) {

    // Include Bootstrap CSS
    $('<link/>', {
        rel: 'stylesheet',
        href: 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        integrity: 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ775/z4Yr3t3Gsapm5lVrMm+4hlgO8aa4CD',
        crossorigin: 'anonymous'
    }).appendTo('head');

    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Target List',
        single_column: true
    });

    // Include the CSS file
    frappe.require("/assets/ride_management/css/tree.css");

    // Create the root node
    let treeContainer = $('<div class="tree"></div>').appendTo(page.body);
    let rootBox = $('<div class="node root">Sales Team</div>').appendTo(treeContainer);
    $('<div class="box amount-box" style="border:1px solid black;padding:5px;margin-bottom:5px;">Amount</div>').appendTo(rootBox);

    // First level nodes (Sales Team1)
    let level1Container = $('<div class="children"></div>').appendTo(rootBox);
    let level1Box = $('<div class="node mt-2">Sales Team1</div>').appendTo(level1Container);
    $('<div class="box amount-box" style="border:1px solid black;padding:5px;margin-bottom:5px;">Amount</div>').appendTo(level1Box);

    // Second level nodes (Sales leaders)
    let leadersContainer = $('<div class="children mt-2 mb-3"></div>').appendTo(level1Box);
    let leaders = ["Sales leader1.1", "Sales leader1.2", "Sales leader1.3"];
    leaders.forEach((leader, index) => {
        let leaderBox = $(`<div class="node mt-3 mb-3" style="margin-bottom:5px;">${leader}</div>`).appendTo(leadersContainer);
        $('<div class="box amount-box" style="border:1px solid black;padding:5px;margin-bottom:5px">Amount</div>').appendTo(leaderBox);

        // Third level nodes (Sales persons)
        let personsContainer = $('<div class="children mb-2"></div>').appendTo(leaderBox);
        let persons = [`Sales person${index+1}.1`, `Sales person${index+1}.2`, `Sales person${index+1}.3`];
        persons.forEach(person => {
            let personBox = $(`<div class="node">${person}</div>`).appendTo(personsContainer);
            $('<div class="box amount-box" style="border:1px solid black;padding:5px;margin-bottom:5px">Amount</div>').appendTo(personBox);
        });
		
    });
	
}



/*
frappe.pages['target-distribution'].on_page_load = function(wrapper) {

    // Include Bootstrap CSS
    $('<link/>', {
        rel: 'stylesheet',
        href: 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        integrity: 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ775/z4Yr3t3Gsapm5lVrMm+4hlgO8aa4CD',
        crossorigin: 'anonymous'
    }).appendTo('head');

    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Target List',
        single_column: true
    });

    // Include the CSS file
    frappe.require("/assets/ride_management/css/tree.css");

    // Create the root node
    let treeContainer = $('<div class="tree"></div>').appendTo(page.body);
    let rootBox = $('<div class="node root">Sales Team</div>').appendTo(treeContainer);
    $('<div class="box amount-box" style="border:1px solid black;padding:5px;margin-bottom:5px;">Amount</div>').appendTo(rootBox);

    // Fetch the sales data from Frappe
    frappe.call({
        method: "frappe.client.get_list",
        args: {
            doctype: "Sales Person", // Adjust to your exact doctype
            fields: ["name", "parent_sales_person"], // Add any other necessary fields
            limit_page_length: 0
        },
        callback: function(response) {
            let salesPersons = response.message;

            // Function to build the hierarchy tree
            function buildTree(salesPersons, parentName) {
                let node = null;
                salesPersons.forEach(function(person) {
                    if (person.parent_sales_person === parentName) {
                        if (!node) {
                            node = $('<div class="children"></div>').appendTo(rootBox);
                        }
                        let personBox = $(`<div class="node mt-2">${person.name}</div>`).appendTo(node);
                        $('<div class="box amount-box" style="border:1px solid black;padding:5px;margin-bottom:5px;">Amount</div>').appendTo(personBox);
                        // Recursively add child sales persons
                        buildTree(salesPersons, person.name, personBox);
                    }
                });
                return node;
            }

            // Build the tree for root level sales persons (those with no parent_sales_person)
            salesPersons.forEach(function(person) {
                if (!person.parent_sales_person) {
                    let level1Box = $(`<div class="node mt-2">${person.name}</div>`).appendTo(rootBox);
                    $('<div class="box amount-box" style="border:1px solid black;padding:5px;margin-bottom:5px;">Amount</div>').appendTo(level1Box);
                    // Recursively add child sales persons
                    buildTree(salesPersons, person.name, level1Box);
                }
            });
        }
    });
}*/



frappe.pages['target-distribution'].on_page_load = function(wrapper) {

    // Include Bootstrap CSS
    $('<link/>', {
        rel: 'stylesheet',
        href: 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        integrity: 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ775/z4Yr3t3Gsapm5lVrMm+4hlgO8aa4CD',
        crossorigin: 'anonymous'
    }).appendTo('head');

    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Target List',
        single_column: true
    });

    // Include the CSS file
    frappe.require("/assets/ride_management/css/tree.css");

    // Create the root node
    let treeContainer = $('<div class="tree"></div>').appendTo(page.body);
    let rootBox = $('<div class="node root">Sales Team</div>').appendTo(treeContainer);
    $('<div class="box amount-box" style="border:1px solid black;padding:5px;margin-bottom:5px;">Amount</div>').appendTo(rootBox);

    // Fetch the sales data from Frappe
    frappe.call({
        method: "frappe.client.get_list",
        args: {
            doctype: "Sales Person",
            fields: ["name", "parent_sales_person"],
            limit_page_length: 0
        },
        callback: function(response) {
            let salesPersons = response.message;

            // Function to build the hierarchy tree
            function buildTree(parentElement, parentName) {
                let children = salesPersons.filter(function(person) {
                    return person.parent_sales_person === parentName;
                });

                if (children.length > 0) {
                    let childContainer = $('<div class="child-container d-flex justify-content-center"></div>').appendTo(parentElement);

                    children.forEach(function(child) {
                        let personBox = $(`<div class="node mt-2">${child.name}</div>`).appendTo(childContainer);
                        $('<div class="box amount-box" style="border:1px solid black;padding:5px;margin-bottom:5px;">Amount</div>').appendTo(personBox);
                        // Recursively add child sales persons
                        buildTree(personBox, child.name);
                    });
                }
            }

            // Start building the tree from the root level (no parent_sales_person)
            buildTree(rootBox, null);
        }
    });
}










