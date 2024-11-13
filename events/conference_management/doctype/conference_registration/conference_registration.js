// Copyright (c) 2024, bwh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Conference Registration", {
	onload(frm) {
		frm.set_value("attendee_count", 0);
	},
	set_attendee_count(frm) {
		console.log("running set attendee count...")
		// calculate total attendees
		const total = frm.doc.attendees.length;
		// set it to attendee count
		frm.set_value("attendee_count", total)
	}
});

frappe.ui.form.on("Registration Attendee", {
	attendees_add(frm) {
		frm.trigger("set_attendee_count");
	},
	attendees_remove(frm) {
		console.log("removing row...")
		frm.trigger("set_attendee_count");
	}
});



