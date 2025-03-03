import frappe
from frappe.model.document import Document

class CarsDetails(Document):
    pass

@frappe.whitelist()
def change_status(car_model):
    frappe.db.set_value('Cars Details', {'car_model': car_model}, 'available', 0)

    return "Car availability status updated successfully!"


@frappe.whitelist()
def get_transmittion_and_price(car_model):
    transmittion = frappe.db.get_value('Cars Details', {'cars_model': car_model}, 'transmittion')

    if transmittion == 'Automatic':
        price = 5999
    elif transmittion == 'Manual':
        price = 3999
    else:
        price = 0  # Default price if transmittion type is not found

    result = {
        'transmittion': transmittion,
        'price': price
    }

    return result


@frappe.whitelist()
def update_car_availability(car_model):
    # Fetch the car document based on the car model (cars_brand)
    car_doc = frappe.get_all('Cars Details', filters={'cars_model': car_model.lower()}, limit_page_length=1)

    # Debugging: Print the result
    print(f"Fetched car documents: {car_doc}")

    if car_doc:
        car_doc = frappe.get_doc('Cars Details', car_doc[0].name)
        
        car_doc.available = 0  # Set checkbox to unchecked
        car_doc.save(ignore_permissions=True)  # Save the updated document (Note: `True` is correct)

        # Return a success message
        return {"message": "Car availability status updated."}
    else:
        return {"message": "Car model not found."}
