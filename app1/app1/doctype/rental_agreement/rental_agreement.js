frappe.ui.form.on('Rental Agreement', {
    refresh: function(frm) {
        frm.set_query('selected_car', 'customers_billing', () => {
            return {
                filters: {
                    transmittion: frm.doc.car_transmission,
                    cars_brand: frm.doc.customers_prefer_car_brand
                }
            }
        })
    },
    // available_cars: function(frm) {
    //     if (frm.doc.available_cars) {
    //         frappe.db.get_value("Cars Details", frm.doc.available_cars, "cars_price", function(value) {
    //             if (value && value.cars_price) {
    //                 frm.set_value("price", value.cars_price); 
    //             } else {
    //                 frappe.msgprint(__("No price found for this item!"), "Error");
    //                 frm.set_value("price", 0);
    //             }
    //         });
    //     }
    // },

    // add_items: function(frm) { 
    //     var rental_start_date = frm.doc.rental_start_date;
    //     var rental_end_date = frm.doc.rental_end_date;
    //     var price = frm.doc.price;
    //     var vehicle_service = frm.doc.vehicle_service;
    //     var available_cars = frm.doc.available_cars;
    //     var selected_car = frm.doc.available_cars;

    //     if (!rental_start_date || !rental_end_date) {
    //         frappe.msgprint(__('Please fill in the rental start and end dates.'));
    //         return;
    //     }

    //     if (vehicle_service == 'With Driver(2999Rs)') {
    //         vehicle_service = 2999;
    //     } else if (vehicle_service == 'Without Driver(Original Price)') {
    //         vehicle_service = 0;
    //     } else {
    //         vehicle_service = 0;
    //     }

    //     var rental_duration_days_diff = frappe.datetime.get_diff(rental_end_date, rental_start_date);
    //     var total_rental_pricepkr = rental_duration_days_diff * price + vehicle_service;

    //     if (rental_duration_days_diff > 0 && price > 0 && vehicle_service >= 0) {
    //         frappe.db.get_value("Cars Details", available_cars, "transmittion", function(value) {
    //             if (value && value.transmittion) {
    //                 var vehicle_type = value.transmittion;

    //                 var new_item = frm.add_child('customers_billing');
    //                 new_item.rental_start_date = rental_start_date;
    //                 new_item.rental_end_date = rental_end_date;
    //                 new_item.price = price;
    //                 new_item.vehicle_service = vehicle_service;
    //                 new_item.total_rental_pricepkr = total_rental_pricepkr;
    //                 new_item.rental_duration_days_ = rental_duration_days_diff;
    //                 new_item.vehicle_type = vehicle_type;
    //                 new_item.selected_car = selected_car;

    //                 frm.refresh_field('customers_billing');
    //                 update_sub_total(frm);
    //             } else {
    //                 frappe.msgprint(__("No transmission data found for this car!"), "Error");
    //             }
    //         });
    //     } else {
    //         frappe.msgprint(__('Please fill in the required fields.'));
    //     }
    // },

    // after_save: function(frm) {
    //     for (let i = 0; i < frm.doc.customers_billing.length; i++) {
    //         let row = frm.doc.customers_billing[i];

    //         if (row.selected_car == 1) {
    //             frappe.model.set_value(row.doctype, row.name, 'selected_car', 0);
    //         }
    //     }
    //     frm.refresh_field('customers_billing');
    // }
});

frappe.ui.form.on('Customer Bill', {
    rental_duration_days_: function(frm, cdt, cdn) {
        // let row = locals[cdt][cdn];
        // if (row.rate) {

            
        // }
        calculation(frm, cdt, cdn)

    }
   
});
frappe.ui.form.on('Customer Bill', {
    select_driver: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.select_driver) {
            row.vehicle_service = 3000
            
        }
    }
   
});

// frappe.ui.form.on('customers_billing', {
//     rental_start_date: function(frm, cdt, cdn) {
//         let row = locals[cdt][cdn];

//         frappe.msgprint('Rental start date has been changed.');
//         console.log('Updated rental_start_date:', row.rental_start_date);
//     }
// });



// function update_rental_cost(frm, cdt, cdn, row) {
//     if (row) {
//         let rental_start_date = row.rental_start_date;
//         let rental_end_date = row.rental_end_date;
//         let vehicle_service = row.vehicle_service;
//         let price = frm.doc.price;
        
//         if (rental_start_date && rental_end_date) {
//             let days_diff = frappe.datetime.get_diff(rental_end_date, rental_start_date);

//             if (days_diff > 0) {
//                 frappe.model.set_value(cdt, cdn, 'rental_duration_days_', days_diff);

//                 let total_cost = (days_diff * price) + vehicle_service;

//                 frappe.model.set_value(cdt, cdn, 'total_rental_pricepkr', total_cost);

//                 frm.refresh_field('customers_billing');
//                 update_sub_total(frm);
//             } else {
//                 frappe.msgprint(__('The rental duration must be greater than zero.'));
//             }
//         } else {
//             frappe.msgprint(__('Please provide both rental start and end dates.'));
//         }
//     }
// }

// function update_sub_total(frm) {
//     let subtotal = 0;

//     frm.doc.customers_billing.forEach(function(row) {
//         if (row.total_rental_pricepkr) {
//             subtotal += row.total_rental_pricepkr;
//         }
//     });

//     frm.set_value('sub_total', subtotal);
//     frm.refresh_field('sub_total');
// }
function calculation(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
            if (row.rate && row.rental_duration_days_) {
                console.log("pok");
                

                
            }   
}

frappe.ui.form.on('Customer Bill', {
    rate: function(frm, cdt, cdn) {
        update_total_rental_price(frm, cdt, cdn);
        update_subtotal(frm); // Update subtotal after each change
    },

    rental_duration_days_: function(frm, cdt, cdn) {
        update_total_rental_price(frm, cdt, cdn);
        update_subtotal(frm); // Update subtotal after each change
    },

    drivers_rent: function(frm, cdt, cdn) {
        update_total_rental_price(frm, cdt, cdn);
        update_subtotal(frm); // Update subtotal after each change
    }
});

// Function to update 'total_rental_pricepkr' for each row
function update_total_rental_price(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    
    if (row.rate && row.rental_duration_days_ && row.drivers_rent) {
        let total_rental_pricepkr = (row.rate * row.rental_duration_days_) + row.drivers_rent;
        frappe.model.set_value(cdt, cdn, 'total_rental_pricepkr', total_rental_pricepkr);
    } else {
        frappe.model.set_value(cdt, cdn, 'total_rental_pricepkr', 0);
    }
}

function update_subtotal(frm) {
    let subtotal = 0;
    
    frm.doc.customer_bill_items.forEach(function(row) {
        subtotal += row.total_rental_pricepkr || 0;  // Add each row's 'total_rental_pricepkr' to subtotal
    });
    
    // Set the subtotal value in the parent form
    frm.set_value('sub_total', subtotal);
    frm.refresh_field('sub_total');  // Refresh the field to show updated value
}


