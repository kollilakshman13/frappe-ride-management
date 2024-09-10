from . import __version__ as app_version

app_name = "ride_management"
app_title = "Ride Management"
app_publisher = "lakshman"
app_description = "a vechicle rental"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "kollilakshman@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ride_management/css/ride_management.css"
# app_include_js = "/assets/ride_management/js/ride_management.js"





# include js, css files in header of web template
#web_include_css = "/assets/ride_management/css/ride_management.css"
# web_include_js = "/assets/ride_management/js/ride_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ride_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
#home_page = "home1"

# website user home page (by Role)
#role_home_page = {
	#"Administrator": "home1",
    #"System Manager":"Solutions"
#}

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ride_management.install.before_install"
# after_install = "ride_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ride_management.uninstall.before_uninstall"
# after_uninstall = "ride_management.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ride_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }
app_include_css = "/assets/ride_management/css/banner.css"

# In your custom app's hooks.py, add:
page_js = {"target-details": "public/js/target_details.js"} 



doc_events= {
    "Job Offer":{
        "before_save":"ride_management.api.get_salary_data"
	} ,
    "Custom DocType": {
        "validate": "ride_management.custom_script.send_email"
    },
    "Event Registration": {
        "on_update": "ride_management.ride_management.doctype.event_registration.event_registration.email_on_approval"
    },
    "Ride order": {
        "on_update": "ride_management.ride_management.doctype.ride_order.ride_order.assign_task"
        
    }
    
}  


# scheduler_events = {
#     "cron": {
#         "* * * * *": [
#             "ride_management.tasks.check_due_reminders"
#         ]
#     }
# }

# scheduler_events = {
#     "cron": {
# 		"* * * * *": [
#         	"ride_management.tasks.check_remainder_notifications"
#     	]
# 	}    
# }



# app_include_js = "/assets/ride_management/js/remainder_notification.js"




#app_include_js = "/assets/ride_management/js/custom.js"



# scheduler_events = {
#     "cron": {
#         "* * * * *": [
#             "ride_management.tasks.send_reminder_notifications"
#         ]
#     }
# }

# scheduler_events = {
#     "cron": {
#         "* * * * *" : [
#             "ride_management.ride_management.doctype.call_list.call_list.send_reminder_notification"
# 		]
# 	}
# }

#app_include_js = "/assets/ride_management/js/notification_update.js"


# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"ride_management.tasks.all"
#	],
#	"daily": [
#		"ride_management.tasks.daily"
#	],
#	"hourly": [
#		"ride_management.tasks.hourly"
#	],
#	"weekly": [
#		"ride_management.tasks.weekly"
#	]
#	"monthly": [
#		"ride_management.tasks.monthly"
#	]
# }
#scheduler_events = {
		#"cron": {
           # " * * * * *":[
            #    "ride_management.tasks.cron"     
			#]
		#}
       
#} 

# Testing
# -------

# before_tests = "ride_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "ride_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "ride_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"ride_management.auth.validate"
# ]


