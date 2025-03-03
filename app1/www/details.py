# about.py
import frappe


def get_context(context):
    # Fetch the "Data" doctype record (make sure this doctype and record exist)
    context.data = frappe.get_all('Sign-up Details',
        fields=['name1', 'email', 'phone', 'address', 'message'])  # Adjust the fields as needed
    return context  




# import frappe
# @frappe.whitelist()

# def get_data(name, email):
#     data = frappe.get_all('Sign-up Details',
#         filters={'name1': name, 'email': email},  # Make sure both name and email are passed in the filter
#         fields=['name1', 'email', 'phone', 'address', 'message'])  # Adjust the fields as needed

#     if data:
#         # You should return the data instead of msgprint here
#         return data
#     else:
#         # Return a message if no data is found
#         return frappe.msgprint('Invalid Data')
