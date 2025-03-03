import frappe
import urllib.parse 

def get_context(context):
    context.cars = frappe.get_all('Car Details', fields=["*"])  # Corrected the assignment

    # product_id = frappe.form_dict.get("id")

    # if product_id:  # Fixed indentation here
    #     # First, URL-decode once
    #     decoded_product_id = urllib.parse.unquote(product_id)
    #     print(f"Decoded product_id: {decoded_product_id}")  # This should print with spaces

    #     # Check if the product_id is still encoded after the first unquote
    #     decoded_product_id = urllib.parse.unquote(decoded_product_id)  # Decode again if needed
    #     print(f"Double-decoded product_id: {decoded_product_id}")  # Print again to ensure spaces

    #     # Now you can use decoded_product_id for further operations
    #     context.product_id = decoded_product_id  # Use this in your query or processing
    #     print(f"product_id")
        
    #     # Ensure the correct field is used for filtering, and the doctype name is consistent
    #     context.product = frappe.get_all(
    #         'Car Details',  # Corrected the doctype name
    #         filters={'cars_model': product_id},  # Assuming 'cars_model' is the correct field
    #         fields=["*"]
    #     )
        
    #     # Check if we found the product
    #     if context.product:
    #         context.product = context.product[0]  # Take the first product
    #         print(f"Product fetched: {context.product}")
    #     else:
    #         print("No product found with that ID.")
    # else:
    #     context.product = None

    return context
    
    # reviews = frappe.get_all(
    #     'Customer Reviews',
    #     filters={'item': id},
    #     fields=['*']
    # )
    # item_docs = []
    # items = frappe.get_all(
    #     'Item',
    #     filters={"variant_of" : id},
    #     fields=['*']
    # )
    # for item in items:
    #     doc = frappe.get_doc("Item", item.name)
    #     item_docs.append(doc)

    # related_items = frappe.get_all(
    #     'Item',
    #     filters={"item_group" : doc.item_group},
    #     fields=['*']
    # )

    # context.update({
    #     "doc": doc,
    #     "items": item_docs,
    #     "related_items": related_items,
    #     "reviews": reviews
    # })

