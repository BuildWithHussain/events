# Copyright (c) 2024, bwh and contributors
# For license information, please see license.txt

import frappe

from frappe.model.document import Document


class ConferenceTicket(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from events.conference_management.doctype.conference_check_in.conference_check_in import ConferenceCheckIn
		from frappe.types import DF

		checkins: DF.Table[ConferenceCheckIn]
		email: DF.Data | None
		full_name: DF.Data
		name: DF.Int | None
		qr_code: DF.AttachImage | None
		registration: DF.Link
		ticket_type: DF.Link
	# end: auto-generated types

	def after_insert(self):
		self.regenerate_qr_code()

	@frappe.whitelist()
	def regenerate_qr_code(self):
		import qrcode
		import io

		img = qrcode.make(f"http://{frappe.local.site}:{frappe.conf.webserver_port}{self.get_url()}")
		output = io.BytesIO()
		img.save(output, format="PNG")
		hex_data = output.getvalue()

		file = frappe.get_doc({
			"doctype": "File",
			"file_name": f"qr-code-{self.name}.png",
			"content": hex_data,
			"attached_to_doctype": "Conference Ticket",
			"attached_to_name": self.name,
			"attached_to_field": "qr_code"
		}).save()

		self.qr_code = file.file_url
		self.save()
