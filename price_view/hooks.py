# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "price_view"
app_title = "Price View"
app_publisher = "PCWired"
app_description = "Display the past Price for an item depending ont he customer"
app_icon = "octicon tag"
app_color = "blue"
app_email = "csxilin@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/price_view/css/price_view.css"
# app_include_js = "/assets/price_view/js/price_view.js"

# include js, css files in header of web template
# web_include_css = "/assets/price_view/css/price_view.css"
# web_include_js = "/assets/price_view/js/price_view.js"

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
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "price_view.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "price_view.install.before_install"
# after_install = "price_view.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "price_view.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"price_view.tasks.all"
# 	],
# 	"daily": [
# 		"price_view.tasks.daily"
# 	],
# 	"hourly": [
# 		"price_view.tasks.hourly"
# 	],
# 	"weekly": [
# 		"price_view.tasks.weekly"
# 	]
# 	"monthly": [
# 		"price_view.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "price_view.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "price_view.event.get_events"
# }

