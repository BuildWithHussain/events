// Copyright (c) 2024, bwh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Conference Ticket", {
	refresh(frm) {
		frm.add_custom_button("Regenerate QR Code", () => {
			frappe.show_alert("Generating QR Code...")
			frm.call("regenerate_qr_code").then(() => {
				frappe.show_alert("QR Code regenerated successfully")
			})
		})
	},
});
