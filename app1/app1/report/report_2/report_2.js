frappe.query_reports["Report 2"] = {
    "filters": [
		{
			"fieldname": "cars_brand",
			"label": __("Car's Brand"),
			"fieldtype": "Link",
			"options": "Car Brand",
			"default": "",
			"reqd": 1,
			"width": "400px"
		},
		{
			"fieldname": "cars_price",
			"label": __("Filter by Price"),
			"fieldtype": "Currency",
			"reqd": 0,
			"width": 400
		},
		// {
		// 	"fieldname": "transmittion",
		// 	"label": __("Filter by Transmission"),
		// 	"fieldtype": "Select",
		// 	"options":"\nAutomatic\nManual",
		// 	"reqd": 0,
		// 	"width": 400
		// }
		{
			"fieldname": "transmittion",
			"label": __("Filter by Transmission"),
			"fieldtype": "Select",
			"options":"\nAutomatic\nManual",
			"reqd": 0,
			"width": 400
		}
    ]
};
