// Listen for the 'call_list_reminder' event
frappe.realtime.on('call_list_reminder', function(data) {
    console.log("Real-time event received:", data);

    // Show the bottom-right notification pop-up
    frappe.show_alert({
        message: __('Reminder: ') + data.message,  // Display the reminder message
        indicator: 'orange'
    }, 5);  // Display for 5 seconds
});

// Ensure that notification counter (bell icon) is updated when a new notification comes in
frappe.realtime.on('notification_update', function() {
    // Refresh the notifications counter
    frappe.call({
        method: "frappe.desk.notifications.get_notifications",
        callback: function(r) {
            if (r.message) {
                frappe.ui.notifications.render_notifications(r.message);
            }
        }
    });
});


// frappe.ready(function() {
//     // Function to check the notification log
//     function check_notifications() {
//         frappe.call({
//             method: "frappe.desk.notifications.get_notifications",
//             callback: function(response) {
//                 let notifications = response.message;
                
//                 // Check if there are new unread notifications
//                 if (notifications && notifications.open_count > 0) {
//                     // Show dialog with the new message
//                     frappe.msgprint({
//                         title: __('Notification'),
//                         message: __('You have a new message'),
//                         indicator: 'green'
//                     });
//                 }
//             }
//         });
//     }

//     // Call the function immediately when the page is ready
//     check_notifications();

//     // Set interval to check the notification log every 30 seconds
//     setInterval(function() {
//         check_notifications();
//     }, 30000);  // Adjust the time interval as needed
// });





frappe.ready(function() {
    // Variable to store the last notification count
    let last_notification_count = 0;

    // Function to check the notification count
    function check_notifications() {
        frappe.call({
            method: "frappe.desk.notifications.get_notifications",
            callback: function(response) {
                let notifications = response.message;
                
                if (notifications && notifications.open_count > last_notification_count) {
                    // Show the alert or dialog for new notifications
                    frappe.show_alert({
                        message: __('You have a new message'),
                        indicator: 'green'
                    }, 5);  // Show for 5 seconds
                    
                    // Optional: Show a dialog with more details
                    frappe.msgprint({
                        title: __('New Notification'),
                        message: __('You have a new message in the notification log.'),
                        indicator: 'green'
                    });

                    // Update the last notification count
                    last_notification_count = notifications.open_count;
                }
            }
        });
    }

    // Real-time listener for notifications
    frappe.realtime.on("notification", (data) => {
        check_notifications(); // Trigger check for new notifications in real-time
    });

    // Check notifications on page load
    check_notifications();

    // Optional: Polling to check notifications every 30 seconds
    setInterval(function() {
        check_notifications();
    }, 30000);  // Adjust the interval if needed
});






