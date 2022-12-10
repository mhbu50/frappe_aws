// Copyright (c) 2022, Accurate Systems and contributors
// For license information, please see license.txt

frappe.ui.form.on('AWS Settings', {
	sync_ec2: function(frm) {
		frm.call({
			doc: frm.doc,
			method: "sync_ec2",
		}).then((r) => {
			frappe.msgprint(__("sync ec2 is Done"));
		});

	}
});
