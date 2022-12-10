// Copyright (c) 2022, Accurate Systems and contributors
// For license information, please see license.txt

frappe.ui.form.on('EC2', {
	activate: function(frm) {

		frm.call({
			doc: frm.doc,
			method: "activate",
		}).then((r) => {
			frappe.msgprint(__("Site has been Activated"));
		});
	},
	deactivate: function(frm) {
		frm.call({
			doc: frm.doc,
			method: "deactivate",
		}).then((r) => {
			frappe.msgprint(__("Site has been Deactivated"));
		});

	}
});
