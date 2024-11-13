# Copyright (c) 2024, bwh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ConferenceCheckIn(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		checkin_at: DF.Datetime
		name: DF.Int | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		scan_hero: DF.Link
	# end: auto-generated types

	pass
