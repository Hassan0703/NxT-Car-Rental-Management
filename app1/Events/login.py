import frappe

@frappe.whitelist()
def form_login(user_name, email):
    user = frappe.get_all('Sign-up Details',
        filters={'name1': user_name},
        fields=['email'])
    
    if user:
        if user[0]['email'] == email:
            return frappe.msgprint(f"'{user_name}' Login Sucessfull")
        else:
            return frappe.msgprint('Wrong Details')
    else:
        return frappe.msgprint('User not found')
