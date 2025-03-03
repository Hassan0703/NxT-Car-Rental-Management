import frappe
import urllib.parse 

def get_context(context):
    product_id = frappe.form_dict.get("id")

    if product_id:  # Fixed indentation here
        decoded_product_id = urllib.parse.unquote(product_id)
        print(f"Decoded product_id: {decoded_product_id}")  # This should print with spaces

        decoded_product_id = urllib.parse.unquote(decoded_product_id)  # Decode again if needed
        print(f"Double-decoded product_id: {decoded_product_id}")  # Print again to ensure spaces

        context.product_id = decoded_product_id  # Use this in your query or processing
        print(f"product_id")
        
        context.product = frappe.get_all(
            'Team',  # Corrected the doctype name
            filters={'name1': product_id},  # Assuming 'cars_model' is the correct field
            fields=["*"]
        )
        
        if context.product:
            context.product = context.product[0]  # Take the first product
            print(f"Product fetched: {context.product}")
        else:
            print("No product found with that ID.")
    else:
        context.product = None

    return context