// Add this in a globally loaded file (e.g., a custom script or a hook into a desk page)

// frappe.realtime.on('notification_update', (data) => {
//     // Reload notifications (this updates the notification bell)
//     frappe.ui.notifications.render_notifications();

//     // Show a pop-up alert for the new notification
//     frappe.show_alert({
//         message: 'You have a new Call List reminder!',
//         indicator: 'blue'
//     }, 5);
// });

// frappe.realtime.on("remainder_notification", (data) => {
//     frappe.show_alert({
//         message: data.message,
//         indicator: 'blue'
//     });
// });

frappe.realtime.on('doc_viewers', function(data) {
    console.log('doc_viewers event received:', data);
    // Display pop-up notification
    frappe.msgprint({
        title: __('Viewer Alert'),
        message: `Viewer for Doc: ${data.docname} - Users: ${data.users.join(', ')}`,
        indicator: 'green'
    });
});

frappe.realtime.on('doc_typers', function(data) {
    console.log('doc_typers event received:', data);
    // Display pop-up notification
    frappe.msgprint({
        title: __('Typer Alert'),
        message: `Typer for Doc: ${data.docname} - Users: ${data.users.join(', ')}`,
        indicator: 'blue'
    });
});



// Global real-time notification listener

$(document).ready(function() {
    // Log to the console to confirm the script is loaded globally
    console.log("Global notification listener loaded.");

    // Listen for real-time events globally
    frappe.realtime.on('call_list_reminder', function(data) {
        console.log("Real-time notification received:", data);

        if (data) {
            console.log("Data received: ", data);
            if (data.message) {
                console.log("Message received: ", data.message);
                // Show an alert notification
                frappe.show_alert({
                    message: __(data.message),
                    indicator: 'green'
                });

                // Optionally, show a pop-up for a more visible notification
                frappe.msgprint({
                    title: __('Global Call Reminder'),
                    indicator: 'green',
                    message: __(data.message)
                });
            } else {
                console.log("No message found in the data.");
            }
        } else {
            console.log("No data received in real-time event.");
        }
    });
});






