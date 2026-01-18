// Lab 13: Callback Function for Billing Completion

function completeBilling(callback) {
    console.log("Billing in progress...");
    callback();
}

function showInvoice() {
    console.log("Invoice generated successfully");
}

completeBilling(showInvoice);
