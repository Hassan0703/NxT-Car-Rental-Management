import frappe

@frappe.whitelist()
def contact_form(name, email, phone, subject, message):
    doc = frappe.get_doc({
        'doctype': 'Cars Contact Us',
        'full_name': name,
        'email': email,
        'subject': subject,
        'phone': phone,
        'message': message
    })

    doc.insert()
    
    return frappe.msgprint(f"'{name}' Your Message have sent Sucessfully. We will contact You as soon as Possible")
    