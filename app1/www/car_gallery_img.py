# about.py
import frappe

def get_context(context):
 context.data = frappe.get_all('Car Details',
     fields=["*"])
 return context
