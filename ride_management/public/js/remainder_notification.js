frappe.realtime.on('remainder_popup', function(message) {
    // Show the popup message when the event is triggered
    frappe.msgprint({
        title: __('Reminder'),
        indicator: 'orange',
        message: message
    });
});



frappe.realtime.on('call_list_reminder', function(data) {
    const message = `Reminder for Call List ${data.docname} is due at ${data.remainder}`;
    frappe.msgprint({
        title: __('Call Reminder'),
        message: message,
        indicator: 'orange'
    });
});
