// Copyright (c) 2024, bwh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Conference", {
	refresh(frm) {
		frm.add_custom_button("Scan Ticket", () => {
			new frappe.ui.Scanner({
				dialog: true,
				on_scan(data) {
					const parts = data.decodedText.split("/")
					const ticketId = parts[parts.length - 1]

					frm.call(
						{
							doc: frm.doc,
							method: "checkin_ticket",
							args: {
								ticket_number: ticketId,
							},
							callback()  {
								frappe.show_alert({
									"message": "Successfully checked in",
									"indicator": "success"
								})
							}
				})
				}
			})
		})
	},
});
