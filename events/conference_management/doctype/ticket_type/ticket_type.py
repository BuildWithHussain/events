# Copyright (c) 2024, bwh and contributors
# For license information, please see license.txt

import frappe

from frappe.model.document import Document


class TicketType(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		conference: DF.Link
		currency: DF.Link | None
		max_limit: DF.Int
		price: DF.Currency
		ticket_type: DF.Literal["Free", "Paid"]
		title: DF.Data
	# end: auto-generated types

	def before_save(self):
		if self.price == 0 and self.ticket_type == "Paid":
			frappe.throw("Paid tickets should have non-zero price!")

	def on_update(self):
		if self.has_value_changed("max_limit") or self.has_value_changed("conference"):
			self.update_total_capacity_in_conference()

	def on_trash(self):
		self.update_total_capacity_in_conference()

	def update_total_capacity_in_conference(self):

		# self.conference
		# get all ticket types that belong to this conference
		all_seats = frappe.get_all(
			"Ticket Type",
			filters={"conference": self.conference},
			pluck="max_limit"
		)
		# sum the max_limit
		max_capacity = sum(all_seats)

		# set it in conference
		frappe.db.set_value(
			"Conference",
			self.conference, "total_capacity", max_capacity
		)
