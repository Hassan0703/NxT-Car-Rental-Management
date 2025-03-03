frappe.ui.form.on("Customer Details", {
    customer_last_name:function(frm){
        if (frm.doc.customer_last_name){
            frm.set_value("full_name", frm.doc.customer_first_name + " " + frm.doc.customer_last_name);
        }
    }
});

