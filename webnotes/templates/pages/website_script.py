# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt 

from __future__ import unicode_literals
import webnotes

no_sitemap = 1
base_template_path = "templates/pages/website_script.js"

def get_context(context):
	script_context = { "javascript": webnotes.conn.get_value('Website Script', None, 'javascript') }
	
	if not webnotes.conf.developer_mode:
		script_context["google_analytics_id"] = webnotes.conn.get_value("Website Settings", "Website Settings",
			"google_analytics_id")
	
	return script_context
