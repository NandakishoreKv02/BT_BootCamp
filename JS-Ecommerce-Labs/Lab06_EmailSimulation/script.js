// Lab 6: Email Simulation and JSON Display

let emailAddress = prompt("Enter your email address:");

if (emailAddress.endsWith("@karunya.edu")) {
    console.log("Invoice sent to:", emailAddress);
} else {
    console.log("Invalid email domain. Email not sent.");
}

let invoiceData = {
    invoiceNumber: "INV1001",
    amount: 3200,
    status: "Paid"
};

console.log("Invoice Data in JSON format:");
console.log(JSON.stringify(invoiceData));

console.log("Thank you for shopping with us!");
