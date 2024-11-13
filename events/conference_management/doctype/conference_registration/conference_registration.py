# Copyright (c) 2024, bwh and contributors
# For license information, please see license.txt

import frappe

from frappe.model.document import Document


class ConferenceRegistration(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from events.conference_management.doctype.registration_attendee.registration_attendee import RegistrationAttendee
		from frappe.types import DF

		amended_from: DF.Link | None
		attendee_count: DF.Int
		attendees: DF.Table[RegistrationAttendee]
		company: DF.Data | None
		conference: DF.Link
		contact_number: DF.Phone | None
		customer_name: DF.Data
		email: DF.Data
		ticket_type: DF.Link
	# end: auto-generated types

	def on_submit(self):
		# iterate over list of attendees
		for attendee in self.attendees:
			# create a ticket for each of them
			ct = frappe.new_doc("Conference Ticket")
			ct.full_name = attendee.full_name
			ct.email = attendee.email
			ct.registration = self.name
			ct.ticket_type = self.ticket_type
			ct.save()
