# Copyright (c) 2024, bwh and contributors
# For license information, please see license.txt

import frappe

from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""

	# frappe.throw(filters.get("my_filter"))

	columns = get_columns()
	data = get_data()

	chart = {
		"type": "donut",
		"data": {
			"labels": [d["conference"] for d in data],
			"datasets": [
				{
					"values": [d["revenue"] for d in data]
				}
			]
		}
	}

	summary = [
		{
			"label": "Total Revenue",
			"value": sum(d["revenue"] for d in data),
			"indicator": "green"
		}
	]

	return columns, data, "Report Message", chart, summary


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": "Conference",
			"fieldname": "conference",
			"fieldtype": "Link",
			"options": "Conference"
		},
		{
			"label": "Revenue",
			"fieldname": "revenue",
			"fieldtype": "Currency"
		}
	]


def get_data() -> list[list]:
	registrations = frappe.get_all(
		"Conference Registration",
		filters={"docstatus": 1},
		fields=["attendee_count", "ticket_type", "conference", "ticket_type.price", "SUM(price * attendee_count) AS revenue"],
		group_by="conference",
	)


	return registrations
