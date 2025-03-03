# about.py
import frappe

def get_context(context):
 context.cars = frappe.data = frappe.get_all('Team',
     fields=["*"])
 return context
