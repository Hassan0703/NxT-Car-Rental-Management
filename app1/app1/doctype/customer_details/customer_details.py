# Copyright (c) 2025, NexTash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CustomerDetails(Document):
    pass

@frappe.whitelist()
def get_car_model(customer_name):
    # Fetch availability_status (car model) based on the customer_name
    car_model = frappe.db.get_value('Customer Details', {'customer_name': customer_name}, 'availability_status')
    return car_model  # Returning availability_status as car model

