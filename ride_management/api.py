
import frappe 

@frappe.whitelist()
def fetch_quotation_item(quotation_name):
    #print("Python method fetch_quotation_item called with quotation_name:", quotation_name)
    sql_query = """
        SELECT 
            q.name,
            it.item_name,
            it.item_code,
            it.item_group,
            it.brand,
            it.qty,
            it.rate,
            it.amount,
            it.description,
            it.conversion_factor,
            it.uom
        FROM 
            `tabQuotation` AS q
        LEFT JOIN 
            `tabQuotation Item` AS it ON q.name = it.parent
        WHERE 
            q.name = %s 
        ORDER BY 
            it.item_code, it.name;       
    """
    
    data = frappe.db.sql(sql_query, (quotation_name),as_dict= True)
    return data
    


@frappe.whitelist()
def fetch_supplier_item(opportunity_name):
    query= """ 
        SELECT opp.name,sq.name,sq.opportunity,sq.supplier,sqi.item_name,sqi.item_code,sqi.qty,sqi.rate,sqi.amount 
        FROM `tabOpportunity` AS opp 
        left join `tabSupplier Quotation` as sq on opp.name=sq.opportunity 
        left join `tabSupplier Quotation Item` as sqi on sq.name=sqi.parent
        where opp.name=%s
        order by sqi.item_name asc
    """
    data1 = frappe.db.sql(query, (opportunity_name), as_dict=True)
    return data1

@frappe.whitelist()
def fetch_quotation_items(quotation_name):
    query = """
        SELECT 
            q.name,
            q.opportunity,
            qi.item_name,
            qi.qty,
            qi.uom,
            qi.rate,
            qi.item_group,
            qi.brand,
            qi.description,
            qi.item_code,
            qi.conversion_factor,
            qi.amount,
            qi.gst_hsn_code,
            sq.name,
            sq.supplier AS supplier_name,
            sqi.item_name AS supplier_quotation_item_name,
            sqi.item_code AS supplier_quotation_item_code,
            sqi.qty AS supplier_quotation_item_quantity,
            sqi.rate AS supplier_quotation_item_rate,
            sqi.amount AS supplier_quotation_item_amount
        FROM 
            `tabQuotation` AS q 
        INNER JOIN 
            `tabQuotation Item` AS qi ON q.name = qi.parent 
        INNER JOIN 
            `tabOpportunity` AS opp ON q.opportunity = opp.name 
        INNER JOIN 
            `tabOpportunity Item` AS oi ON opp.name = oi.parent 
            AND qi.item_name = oi.item_name 
            AND qi.description = oi.description 
            AND qi.qty = oi.qty
        INNER JOIN  
            `tabSupplier Quotation` AS sq ON q.opportunity = sq.opportunity 
        INNER JOIN 
            `tabSupplier Quotation Item` AS sqi ON sq.name = sqi.parent 
            AND qi.item_name = sqi.item_name 
            AND qi.description = sqi.description 
            AND qi.qty = sqi.qty  
        WHERE 
            q.name = %s AND sqi.recommended = 1 
        GROUP BY 
            q.name,qi.name       
        ORDER BY 
            q.name, qi.item_name, qi.rate, qi.qty ASC;
    """

    data=frappe.db.sql(query,{quotation_name,},as_dict=True)
    return data



@frappe.whitelist()
def fetch_cof_item(cof_id):
    
    sql_query = """
        SELECT 
            q.name,
            q.party_name,
            q.quotation,
            it.item_name,
            it.item_code,
            it.item_group,
            it.brand,
            it.qty,
            it.rate,
            it.amount,
            it.description,
            it.uom,
            it.conversion_factor,
            it.price_list_rate
        FROM 
            `tabCustomer Order Form` AS q
        LEFT JOIN 
            `tabCustomer Order Item` AS it ON q.name = it.parent 
        WHERE 
            q.name = %s  
        ORDER BY 
            it.item_name,it.item_code,it.qty,it.rate;       
    """
    
    data = frappe.db.sql(sql_query, (cof_id,),as_dict= True)
    return data   






# In ride_management/api.py

import frappe

@frappe.whitelist()
def address_data(doctype, docname):
    addresses = frappe.get_all('Address', filters={'link_doctype': doctype, 'link_name': docname}, fields=['name', 'address_title', 'address_line1', 'address_line2', 'city', 'state', 'country', 'pincode', 'phone', 'email_id'])
    
    # Fetch contact details
    contacts = frappe.get_all('Contact', filters={'link_doctype': doctype, 'link_name': docname}, fields=['name', 'first_name','salutation', 'last_name','middle_name', 'phone', 'email_id'])
    
    return {
        "addresses": addresses,
        "contacts": contacts
    }


import frappe

@frappe.whitelist(allow_guest=True)
def get_job_details(job_id):
    if job_id:
        job = frappe.get_doc("Job Opening", job_id)
        if job:
            return {
                "job_id": job_id,
                "job_title": job.job_title,
                "description": job.description,
                "department": job.department,
                "lower_range": job.lower_range,
                "upper_range": job.upper_range
            }
    return {"error": "Job not found"}

#email group start
import frappe

@frappe.whitelist()
def get_column_list(doctype):
    try:
        # Get meta information for the given doctype
        meta = frappe.get_meta(doctype)
        # Extract field names and labels
        fields = [{'label': df.label, 'fieldname': df.fieldname} for df in meta.fields]
        return fields
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), 'get_column_list')
        return []

@frappe.whitelist()
def get_field_values(doctype, fieldname):
    values = frappe.db.get_list(doctype,fields= [fieldname], distinct= True)
    return [value[fieldname] for value in values]
 
import frappe

@frappe.whitelist()
def get_field_names(doctype):
    meta = frappe.get_meta(doctype)
    fieldnames = [field.fieldname for field in meta.fields if field.fieldtype not in ['Table', 'Table MultiSelect']]
    return fieldnames

@frappe.whitelist()
def get_field_values(doctype, fieldname):
    values = frappe.get_all(doctype, fields=[fieldname], distinct=True)
    return [value[fieldname] for value in values]

@frappe.whitelist()

def get_distinct_field_value(doctype, field_name, start=0, page_length=20, search_term=''):

    if not doctype or not field_name:

        return []
    filters = f"{field_name} IS NOT NULL"

    if search_term:
        filters += f" AND {field_name} LIKE '%{search_term}%'"
    query = f"""
        SELECT DISTINCT {field_name}
        FROM `tab{doctype}`
        WHERE {filters}
        ORDER BY {field_name}
        LIMIT {start}, {page_length}
    """
    results = frappe.db.sql(query, as_dict=True)
    return [d[field_name] for d in results]

#email group end


# target list start
# ride_management/api.py

import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_sub_target_details(name, fiscal_year):
    # Ensure that `name` and `fiscal_year` are provided
    if not name or not fiscal_year:
        frappe.throw(_("Name and Fiscal Year are required"))

    # Query to fetch sub-target details based on the name and fiscal year
    sub_targets = frappe.get_all('Sub Target', filters={
        'target_name': name,
        'fiscal_year': fiscal_year
    }, fields=[
        'name', 'category_type', 'category', 'fiscal_year',
        'target_amount', 'target_distribution', 'topline_target', 'bottomline_target'
    ])

    if not sub_targets:
        return {
            'sub_target': []
        }

    return {
        'sub_target': sub_targets
    }




import frappe

@frappe.whitelist()
def get_sub_targets(sales_person_id, fiscal_year):
    if not frappe.has_permission("Sub Target Details List", "read"):
        frappe.throw(_("You do not have enough permissions to access this resource. Please contact your manager to get access."))

    fields = [
        "category_type",
        "category",
        "fiscal_year",
        "target_distribution",
        "topline_target",
        "bottomline_target"
    ]

    sub_targets = frappe.get_list("Sub Target Details List",filters={"fiscal_year": fiscal_year},fields=fields)
    return sub_targets

@frappe.whitelist()
def add_sub_target(details):
    if not frappe.has_permission("Sub Target Details List", "write"):
        frappe.throw(_("You do not have enough permissions to perform this action. Please contact your manager to get access."))

    details = frappe.parse_json(details)
    
    sub_target = frappe.get_doc({
        "doctype": "Sub Target Details List",
        "sales_person": details["sales_person"],
        "fiscal_year": details["fiscal_year"],
        "category_type": details["category_type"],
        "category": details["category"],
        "target_distribution": details["target_distribution"],
        "topline_target": details["topline_target"],
        "bottomline_target": details["bottomline_target"]
    })
    sub_target.insert()
    frappe.db.commit()
    return sub_target


# @frappe.whitelist()
# def save_sub_targets(sub_targets):
#     # Log the raw form data
#     frappe.log_error(frappe.as_json(sub_targets), "Sub Targets - Raw Form Data")
    
#     if isinstance(sub_targets, str):
#         sub_targets = frappe.parse_json(sub_targets)
    
#     # Log the parsed form data
#     frappe.log_error(frappe.as_json(sub_targets), "Sub Targets - Parsed Form Data")

#     for sub_target in sub_targets:
#         sales_person_id = sub_target.get('sales_person_id')
#         category_type = sub_target.get('category_type')
#         category = sub_target.get('category')
#         fiscal_year = sub_target.get('fiscal_year')
#         target_amount = sub_target.get('target_amount')
#         target_distribution = sub_target.get('target_distribution')
#         topline_target = sub_target.get('topline_target')
#         bottomline_target = sub_target.get('bottomline_target')

#         # Find the parent document (e.g., Sales Person) where sub targets should be linked
#         parent_doc = frappe.get_doc("Target List", sales_person_id)
        
#         # Check if the sub target already exists in the child table
#         existing_sub_target = None
#         for item in parent_doc.get("sub_targets"):
#             if item.category_type == category_type and item.category == category and item.fiscal_year == fiscal_year:
#                 existing_sub_target = item
#                 break
        
#         if existing_sub_target:
#             # Update existing sub target
#             existing_sub_target.target_amount = target_amount
#             existing_sub_target.target_distribution = target_distribution
#             existing_sub_target.topline_target = topline_target
#             existing_sub_target.bottomline_target = bottomline_target
#         else:
#             # Add a new sub target to the child table
#             parent_doc.append("sub_targets", {
#                 "category_type": category_type,
#                 "category": category,
#                 "fiscal_year": fiscal_year,
#                 "target_amount": target_amount,
#                 "target_distribution": target_distribution,
#                 "topline_target": topline_target,
#                 "bottomline_target": bottomline_target
#             })

#         # Save the parent document, which will also save the child table
#         parent_doc.save()

#     frappe.db.commit()
#     return {"status": "success", "message": "Sub Targets saved successfully"}




   


@frappe.whitelist()
def save_sub_targets(sub_targets):
    # Log the incoming sub_targets argument
    frappe.log_error(frappe.as_json(sub_targets), "Sub Targets - Initial Data")
    
    if not sub_targets:
        frappe.throw("Sub targets data is missing.")

    if isinstance(sub_targets, str):
        sub_targets = frappe.parse_json(sub_targets)
    
    # Log the parsed form data
    frappe.log_error(frappe.as_json(sub_targets), "Sub Targets - Parsed Form Data")

    # Process the sub_targets as per your existing code...
    for sub_target in sub_targets:
        sales_person_id = sub_target.get('sales_person_id')
        category_type = sub_target.get('category_type')
        category = sub_target.get('category')
        fiscal_year = sub_target.get('fiscal_year')
        target_amount = sub_target.get('target_amount')
        target_distribution = sub_target.get('target_distribution')
        topline_target = sub_target.get('topline_target')
        bottomline_target = sub_target.get('bottomline_target')

        parent_doc = frappe.get_doc("Target List", sales_person_id)
        
        existing_sub_target = None
        for item in parent_doc.get("sub_targets"):
            if item.category_type == category_type and item.category == category and item.fiscal_year == fiscal_year:
                existing_sub_target = item
                break
        
        if existing_sub_target:
            existing_sub_target.target_amount = target_amount
            existing_sub_target.target_distribution = target_distribution
            existing_sub_target.topline_target = topline_target
            existing_sub_target.bottomline_target = bottomline_target
        else:
            parent_doc.append("sub_targets", {
                "category_type": category_type,
                "category": category,
                "fiscal_year": fiscal_year,
                "target_amount": target_amount,
                "target_distribution": target_distribution,
                "topline_target": topline_target,
                "bottomline_target": bottomline_target
            })

        parent_doc.save()

    frappe.db.commit()
    return {"status": "success", "message": "Sub Targets saved successfully"}






#opportunity
# import frappe

# @frappe.whitelist()
# def get_salesperson_details(user_id):
#     """
#     Fetch details of the salesperson including their parent salesperson.
#     """
#     # Fetch the salesperson associated with the user_id
#     salesperson = frappe.get_value("Sales Person", {"user": user_id}, "name")
#     if salesperson:
#         # Get the parent salesperson of this salesperson
#         parent_salesperson = frappe.get_value("Sales Person", {"name": salesperson}, "parent_salesperson")
#     else:
#         salesperson = None
#         parent_salesperson = None
    
#     return {
#         "name": salesperson,
#         "parent_salesperson": parent_salesperson
#     }

        










