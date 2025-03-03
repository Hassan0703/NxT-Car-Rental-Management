# import frappe

# def execute(filters=None):
#     # Define the columns for the report
#     columns = [
#         {
#             'fieldname': 'cars_registration_number',
#             'label': ('Cars Registration Number'),
#             'fieldtype': 'Data',
#             'width': 243
#         },
#         {
#             'fieldname': 'transmittion',
#             'label': ('Cars Transmission'),
#             'fieldtype': 'Data',
#             'width': 243
#         },
#         {
#             'fieldname': 'cars_price',
#             'label': ('Cars Price'),
#             'fieldtype': 'Data',
#             'width': 243
#         },
#         {
#             'fieldname': 'cars_model',
#             'label': ('Cars Model'),
#             'fieldtype': 'Data',
#             'width': 243
#         },
#         {
#             'fieldname': 'cars_brand',
#             'label': ('Cars Brand'),
#             'fieldtype': 'Data',
#             'width': 243
#         }
#     ]

#     # Initialize conditions for filters
#     conditions = {}

#     # Check if filters are provided
#     if filters:
#         # Get filter values
#         car_brand = filters.get("cars_brand")
#         price = filters.get("cars_price")
#         transmittion = filters.get("transmittion")

#         # Apply the filters to conditions dictionary
#         if car_brand:
#             conditions["cars_brand"] = car_brand
        
#         if price:
#             conditions["cars_price"] = ["<=", price]
        
#         if transmittion:
#             conditions["transmittion"] = transmittion

#     # Fetch data from the Cars Details doctype
#     data = frappe.db.get_all(
#         "Cars Details",  # The Doctype you're fetching from
#         filters=conditions,  # Apply the filters to the conditions
#         fields=["cars_brand", "cars_model", "cars_registration_number", "transmittion", "cars_price"]  # Fields to retrieve
#     )
    
#     return columns, data


# -------------------------------------------------------------------------------------------

# import frappe

# def execute(filters=None):
# 	if not filters: filters = {}

# 	data, coloumns = [], []

# 	coloumns = get_colomns()
# 	cars_data = get_cars_data(filters)

# 	if not cars_data:
# 		frappe.frappe.msgprint(_('No record Found'))
# 		return coloumns, cars_data

# 	data = []
# 	for d in cars_data:
# 		row = frappe._dict({
# 			'brand': d.cars_brand,
# 			'price': d.cars_price,
# 			'transmission': d.transmittion
# 			})
# 		data.append(row)

# def get_cars_data(filters):
# 	conditions = get_conditions(filters)
# 	data = frappe.data = frappe.get_all('Cars Details',
# 		fields=['cars_brand', 'cars_price', 'transmittion'],
# 		filters= conditions
# 	)
# 	return data
		
# def get_conditions(filters):
# 	conditions = {}
# 	for key, value in filters.item():
# 		if filters.get(key):
# 			conditions[key] = value

# 	return conditions

# ------------------------------------------------------------------------------------------------

# import frappe
# def execute(filters=None):

# 	def get_car_details(filters):
# 		# Initialize an empty list to store the conditions
# 		conditions = []

# 		# Add conditions based on filters (this is dynamic based on user input)
# 		if filters.get("cars_brand"):
# 			conditions.append(f"cars_brand = '{filters['cars_brand']}'")
		
# 		if filters.get("cars_price"):
# 			conditions.append(f"cars_price = {filters['cars_price']}")
		
# 		if filters.get("transmittion"):
# 			conditions.append(f"transmittion = '{filters['transmittion']}'")
# 	def get_car_details(filters):
# 		# Initialize an empty list to store the conditions
# 		conditions = []

# 		# Add conditions based on filters (this is dynamic based on user input)
# 		if filters.get("cars_brand"):
# 			conditions.append(f"cars_brand = '{filters['cars_brand']}'")
		
# 		if filters.get("cars_price"):
# 			conditions.append(f"cars_price = {filters['cars_price']}")
		
# 		if filters.get("transmittion"):
# 			conditions.append(f"transmittion = '{filters['transmittion']}'")

# 		# Convert conditions to a string with 'AND' to combine them
# 		condition_str = " AND ".join(conditions) if conditions else "1=1"  # "1=1" is always true, to handle the case of no filters

# 		# Write the SQL query to fetch the car details based on the conditions
# 		sql_query = f"""
# 		SELECT cars_brand, cars_price, transmittion 
# 		FROM `tabCars Details` 
# 		WHERE {condition_str}
# 		"""

# 		# Run the query using frappe.db.sql() and fetch the data
# 		data = frappe.db.sql(sql_query, as_dict=True)

# 		# Return the result
# 		return data

	# # # Example usage
	# # filters = {
	# #     'cars_brand': 'Toyota',  # You can pass different filters here
	# #     'cars_price': 25000,
	# #     'transmittion': 'Automatic'
	# # }

	# car_details = get_car_details(filters)
	# for car in car_details:
	# 	print(car)

# ----------------------------------------------------------------------------------------------
# import frappe
# def execute(filters=None):

# 	def get_car_details(filters):
# 		# Use frappe.get_all() to dynamically build filters
# 		car_details = frappe.get_all(
# 			'Cars Details',  # Doctype
# 			fields=['cars_brand', 'cars_price', 'transmittion'],  # Fields to retrieve
# 			filters=filters  # Pass filters as a dictionary
# 		)
		
# 		return car_details

# 	# # Example usage
# 	# filters = {
# 	# 	'cars_brand': 'Toyota',  # You can pass different filters here
# 	# 	'cars_price': 25000,
# 	# 	'transmittion': 'Automatic'
# 	# }

# 	car_details = get_car_details(filters)
# 	for car in car_details:
# 		print(car)



import frappe

def execute(filters=None):
    # Fetch data from different doctypes
    car_data = frappe.get_all(
        'Cars Details',
        fields=['cars_brand', 'cars_model', 'transmittion', 'cars_price']
    )

    customers = frappe.get_all(
        'Customer Details', 
        fields=['full_name', 'customer_contact_number', 'customers_driving_licence_number']
    )
    frappe.frappe.msgprint(f"{customers}")
    

    agreement_data = frappe.get_all(
        'Rental Agreement',
        fields=['rental_start_date']
    )

    report_data = []

    # Iterate through car data and process it
    for car in car_data:
        # Assuming we want to combine information from 'Cars Details' and 'Customer Details'
        # You can adjust the matching criteria based on your business logic
        customer_name = None
        for cust in customers:
            # Assuming you match based on a field, you could adjust the match logic if needed
            if car['cars_brand'] == cust['full_name']:  # For example, matching car's brand with customer's full name
                customer_name = cust['full_name']
                break  # Exit once a match is found

        # Fetch the rental agreement details related to this car
        rental_start_date = None
        for agreement in agreement_data:
            # Assuming we match based on rental start date (or any other condition that makes sense)
            if agreement['rental_start_date']:  # Just a placeholder condition for matching
                rental_start_date = agreement['rental_start_date']
                break  # Exit once a match is found
        
        # Adding the data to the report data
        report_data.append({
            'car_brand': car['cars_brand'],
            'car_model': car['cars_model'],
            'transmission': car['transmittion'],
            'price': car['cars_price'],
            'customer_name': customer_name,
            'rental_start_date': rental_start_date
        })

    # Define the columns for the report
    columns = get_columns()

    return columns, report_data

def get_columns():
    columns = [
        {"fieldname": "car_brand", "label": "Car Brand", "fieldtype": "Data"},
        {"fieldname": "car_model", "label": "Car Model", "fieldtype": "Data"},
        {"fieldname": "transmission", "label": "Transmission", "fieldtype": "Data"},
        {"fieldname": "customer_first_name", "label": "customer_first_name", "fieldtype": "Data"},
        {"fieldname": "customer_contact_number", "label": "customer_contact_number", "fieldtype": "Phone"},
        {"fieldname": "customers_driving_licence_number", "label": "customers_driving_licence_number", "fieldtype": "Da"},
        {"fieldname": "customer_name", "label": "Customer Name", "fieldtype": "Data"},
        {"fieldname": "rental_start_date", "label": "Rental Start Date", "fieldtype": "Date"}
    ]
    return columns
