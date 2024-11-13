# Copyright (c) 2024, bwh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ConferenceAppSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		api_secret: DF.Password | None
		attach_ticket_in_email: DF.Check
	# end: auto-generated types

	pass
