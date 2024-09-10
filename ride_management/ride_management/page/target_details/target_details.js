// frappe.pages['target-details'].on_page_load = function(wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Targets',
// 		single_column: true
// 	});
// }


frappe.pages['target-details'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Target List',
        single_column: true
    });

    console.log("Page loaded");

    if (!$.fn.jstree) {
        console.log("jsTree library not loaded, loading now...");
        $.getScript("https://cdnjs.cloudflare.com/ajax/libs/jstree/3.3.12/jstree.min.js", function() {
            $('head').append('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jstree/3.3.12/themes/default/style.min.css" type="text/css" />');
            initPage();
        });
    } else {
        console.log("jsTree library already loaded");
        initPage();
    }

    function initPage() {
        console.log("Initializing page");

        $(wrapper).find('.layout-main-section').append('<div id="hierarchical-list"></div>');
        $(wrapper).find('.layout-main-section').append('<button id="save-targets" class="btn btn-primary" style="margin-top: 20px;">Save Targets</button>');

        fetchFiscalYears().then(fiscalYears => {
            frappe.call({
                method: "frappe.client.get_list",
                args: {
                    doctype: "Sales Person",
                    fields: ["name", "parent_sales_person"],
                    limit_page_length: 1000
                },
                callback: function(response) {
                    console.log("Fetched sales person data", response);
                    if (response.message) {
                        let salesPersons = response.message;
                        let treeData = buildTree(salesPersons);
                        console.log("Built tree data", treeData);
                        renderTree(treeData, fiscalYears);
                    }
                }
            });
        });
    }

    function fetchFiscalYears() {
        return new Promise((resolve, reject) => {
            frappe.call({
                method: "frappe.client.get_list",
                args: {
                    doctype: "Fiscal Year",
                    fields: ["name"],
                    order_by: "name asc"
                },
                callback: function(response) {
                    if (response.message) {
                        let fiscalYears = response.message.map(fy => fy.name);
                        console.log("Fetched fiscal years", fiscalYears);
                        resolve(fiscalYears);
                    } else {
                        reject("Failed to fetch fiscal years");
                    }
                }
            });
        });
    }

    function buildTree(salesPersons) {
        let map = {};
        let node;
        let roots = [];

        salesPersons.forEach(function(salesPerson) {
            map[salesPerson.name] = salesPerson;
            salesPerson.children = [];
        });

        salesPersons.forEach(function(salesPerson) {
            if (salesPerson.parent_sales_person) {
                node = map[salesPerson.parent_sales_person];
                if (node) {
                    node.children.push(salesPerson);
                }
            } else {
                roots.push(salesPerson);
            }
        });

        return roots;
    }

    function renderTree(treeData, fiscalYears) {
        console.log("Rendering tree", treeData);
        $('#hierarchical-list').jstree({
            'core': {
                'data': formatTreeData(treeData)
            }
        })
        .on('loaded.jstree', function() {
            console.log("Tree loaded");
            $(this).jstree('close_all');
        })
        .on('after_open.jstree', function(event, data) {
            console.log("Node opened", data.node);
            addInputFields(data.node, fiscalYears);
        });
    }

    function formatTreeData(treeData) {
        let jsTreeData = [];

        function traverse(node) {
            jsTreeData.push({
                id: node.name,
                parent: node.parent_sales_person || '#',
                text: node.name
            });

            if (node.children && node.children.length) {
                node.children.forEach(traverse);
            }
        }

        treeData.forEach(traverse);
        console.log("Formatted tree data for jsTree", jsTreeData);
        return jsTreeData;
    }

    function addInputFields(node, fiscalYears) {
        let nodeId = node.id.replace(/\s/g, '\\ ');
        let $node = $('#' + nodeId + '_anchor');
        console.log("Adding input fields to node", nodeId, $node);

        function addFieldsToNode(node) {
            let nodeId = node.id.replace(/\s/g, '\\ ');
            let $node = $('#' + nodeId + '_anchor');
            if ($node.length && $node.siblings('.input-fields').length === 0) {
                let fiscalYearOptions = fiscalYears.map(fy => `<option value="${fy}">${fy}</option>`).join('');
                $node.after(`
                    <div class="input-fields" style="display: inline-block; margin-left: 10px;">
                        <select class="form-control fiscal-year" data-id="${node.id}" style="display: inline-block; width: 120px; margin-right: 10px;">
                            <option value="">Select Fiscal Year</option>
                            ${fiscalYearOptions}
                        </select>
                        <input type="text" class="form-control topline-target" placeholder="Topline Target" data-id="${node.id}" style="display: inline-block; width: 120px; margin-right: 10px;" />
                        <input type="text" class="form-control bottomline-target" placeholder="Bottomline Target" data-id="${node.id}" style="display: inline-block; width: 120px; margin-right: 10px;" />
                        <button class="btn btn-primary save-target">Save</button>
                        <button class="btn btn-secondary edit-target" style="display: none;">Edit Targets</button>
                        <button class="btn btn-secondary view-sub-targets" style="display: none;">View Sub-Targets</button>
                    </div>
                `);
                console.log("Input fields added to node", nodeId);
            } else {
                console.log("Input fields already exist or node not found for", nodeId);
            }
        }

        addFieldsToNode(node);

        if (node.children && node.children.length) {
            node.children.forEach(childNodeId => {
                let childNode = $('#hierarchical-list').jstree(true).get_node(childNodeId);
                if (childNode) {
                    addFieldsToNode(childNode);
                }
            });
        }
    }

    $(document).on('click', '.save-target', function() {
        console.log("Save button clicked");
        let targets = [];

        $('.input-fields').each(function() {
            let salesPersonId = $(this).find('.fiscal-year').data('id');
            let fiscalYear = $(this).find('.fiscal-year').val();
            let toplineTarget = $(this).find('.topline-target').val();
            let bottomlineTarget = $(this).find('.bottomline-target').val();

            if (fiscalYear && toplineTarget && bottomlineTarget) {
                targets.push({
                    sales_person: salesPersonId,
                    fiscal_year: fiscalYear,
                    topline_target: toplineTarget,
                    bottomline_target: bottomlineTarget
                });
            }
        });

        console.log("Targets to be saved", targets);

        targets.forEach(target => {
            frappe.call({
                method: "frappe.client.insert",
                args: {
                    doc: {
                        doctype: "Target List",
                        sales_person: target.sales_person,
                        fiscal_year: target.fiscal_year,
                        topline_target: target.topline_target,
                        bottomline_target: target.bottomline_target
                    }
                },
                callback: function(response) {
                    console.log("Target saved", response);
                    frappe.msgprint("Targets saved successfully");
                    $(`[data-id="${target.sales_person}"]`).closest('.input-fields').find('.edit-target, .view-sub-targets').show();
                    $(`[data-id="${target.sales_person}"]`).closest('.input-fields').find('.save-target').hide();
                }
            });
        });
    });

    
    $(document).on('click', '.view-sub-targets', function() {
        let salesPersonId = $(this).siblings('.fiscal-year').data('id');
        let fiscalYear = $(this).siblings('.fiscal-year').val();
    
        frappe.call({
            method: "ride_management.api.get_sub_targets",
            args: {
                sales_person_id: salesPersonId,
                fiscal_year: fiscalYear
            },
            callback: function(response) {
                let subTargetsHtml = `
                    <tr>
                        <td><input type="text" class="form-control category_type" placeholder="Category Type" /></td>
                        <td><input type="text" class="form-control category" placeholder="Category" /></td>
                        <td><input type="text" class="form-control fiscal_year" value="${fiscalYear}" readonly /></td>
                        <td><input type="text" class="form-control target_amount" placeholder="Target Amount" /></td>
                        <td><input type="text" class="form-control target_distribution" placeholder="Target Distribution" /></td>
                        <td><input type="text" class="form-control topline_target" placeholder="Topline Target" /></td>
                        <td><input type="text" class="form-control bottomline_target" placeholder="Bottomline Target" /></td>
                        <td><button class="btn btn-danger remove-row">Remove</button></td>
                    </tr>
                `;
    
                if (response.message) {
                    let subTargets = response.message;
                    subTargetsHtml += subTargets.map(subTarget => `
                        <tr>
                            <td><input type="text" class="form-control category_type" value="${subTarget.category_type}" /></td>
                            <td><input type="text" class="form-control category" value="${subTarget.category}" /></td>
                            <td><input type="text" class="form-control fiscal_year" value="${subTarget.fiscal_year}" readonly /></td>
                            <td><input type="text" class="form-control target_amount" value="${subTarget.target_amount}" /></td>
                            <td><input type="text" class="form-control target_distribution" value="${subTarget.target_distribution}" /></td>
                            <td><input type="text" class="form-control topline_target" value="${subTarget.topline_target}" /></td>
                            <td><input type="text" class="form-control bottomline_target" value="${subTarget.bottomline_target}" /></td>
                            <td><button class="btn btn-danger remove-row">Remove</button></td>
                        </tr>
                    `).join('');
                }
    
                frappe.msgprint({
                    message: `
                        <h4>Sub Targets for ${salesPersonId} (${fiscalYear})</h4>
                        <div style="width: 800px;"> <!-- Adjust width here -->
                            <table class="table table-bordered">
                                <thead>
                                    <tr>
                                        <th>Category Type</th>
                                        <th>Category</th>
                                        <th>Fiscal Year</th>
                                        <th>Target Amount</th>
                                        <th>Target Distribution</th>
                                        <th>Topline Target</th>
                                        <th>Bottomline Target</th>
                                        <th>Action</th>
                                    </tr>
                                </thead>
                                <tbody id="sub-targets-table-body">
                                    ${subTargetsHtml}
                                </tbody>
                            </table>
                            <button id="add-row" class="btn btn-primary">Add Row</button>
                            <button id="save-sub-targets" class="btn btn-primary">Save Sub Targets</button>
                        </div>
                    `,
                    title: 'Sub Targets',
                    wide: true
                });
    
                $('#add-row').on('click', function() {
                    $('#sub-targets-table-body').append(`
                        <tr>
                            <td><input type="text" class="form-control category_type" placeholder="Category Type" /></td>
                            <td><input type="text" class="form-control category" placeholder="Category" /></td>
                            <td><input type="text" class="form-control fiscal_year" value="${fiscalYear}" readonly /></td>
                            <td><input type="text" class="form-control target_amount" placeholder="Target Amount" /></td>
                            <td><input type="text" class="form-control target_distribution" placeholder="Target Distribution" /></td>
                            <td><input type="text" class="form-control topline_target" placeholder="Topline Target" /></td>
                            <td><input type="text" class="form-control bottomline_target" placeholder="Bottomline Target" /></td>
                            <td><button class="btn btn-danger remove-row">Remove</button></td>
                        </tr>
                    `);
                });
    
                // Remove row functionality
                $(document).on('click', '.remove-row', function() {
                    $(this).closest('tr').remove();
                });
                $(document).ready(function() {
                    ('#save-sub-targets').on('click', function() {
                        console.log("save sub targets clicked")
                        let subTargets = [];
        
                        $('#sub-targets-table-body tr').each(function() {
                            let categoryType = $(this).find('.category_type').val();
                            let category = $(this).find('.category').val();
                            let fiscalYear = $(this).find('.fiscal_year').val();
                            let targetAmount = $(this).find('.target_amount').val();
                            let targetDistribution = $(this).find('.target_distribution').val();
                            let toplineTarget = $(this).find('.topline_target').val();
                            let bottomlineTarget = $(this).find('.bottomline_target').val();
        
                            if (categoryType && category && fiscalYear && targetAmount && targetDistribution && toplineTarget && bottomlineTarget) {
                                subTargets.push({
                                    category_type: categoryType,
                                    category: category,
                                    fiscal_year: fiscalYear,
                                    target_amount: targetAmount,
                                    target_distribution: targetDistribution,
                                    topline_target: toplineTarget,
                                    bottomline_target: bottomlineTarget
                                });
                            }
                        });
        
                        frappe.call({
                            method: "ride_management.api.save_sub_targets",
                            args: {
                                sub_targets: subTargets
                            },
                            callback: function(response) {
                                console.log("Sub Targets saved", response);
                                frappe.msgprint("Sub Targets saved successfully");
                            }
                        });
                    });
                });       
            },
            error: function(error) {
                console.error("Error fetching sub-targets:", error);
                frappe.msgprint("You do not have enough permissions to access this resource. Please contact your manager to get access.");
            }
        });
    });
   
};














