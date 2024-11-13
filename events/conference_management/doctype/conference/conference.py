# Copyright (c) 2024, bwh and contributors
# For license information, please see license.txt

import frappe

from frappe.website.website_generator import WebsiteGenerator


class Conference(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		approved: DF.Check
		banner_image: DF.AttachImage | None
		city: DF.Data | None
		description: DF.TextEditor
		ends_on: DF.Datetime
		is_published: DF.Check
		livestream_url: DF.Data | None
		mode: DF.Literal["Online", "In Person"]
		route: DF.Data | None
		starts_on: DF.Datetime
		total_capacity: DF.Int
		type: DF.Literal["Free", "Paid"]
		venue: DF.SmallText | None
	# end: auto-generated types

	@frappe.whitelist()
	def checkin_ticket(self, ticket_number):
		ticket = frappe.get_doc("Conference Ticket", ticket_number)
		ticket.append("checkins", {
			"scan_hero": frappe.session.user,
			"checkin_at": frappe.utils.now()
		})
		ticket.save()

