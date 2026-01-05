// Lab 5: Generate Final Invoice

let cart = [];
let grandTotal = 0;
let addMore = true;

// Step 1: Cart input
while (addMore) {
    let itemCode = prompt("Enter item code:");
    let description = prompt("Enter item description:");
    let quantity = Number(prompt("Enter quantity:"));
    let pricePerUnit = Number(prompt("Enter price per unit:"));

    let totalPrice = quantity * pricePerUnit;

    cart.push({
        itemCode: itemCode,
        description: description,
        quantity: quantity,
        pricePerUnit: pricePerUnit,
        totalPrice: totalPrice
    });

    let choice = prompt("Do you want to add another item? (yes/no)");
    if (choice.toLowerCase() !== "yes") {
        addMore = false;
    }
}

// Step 2: Calculate subtotal
for (let i = 0; i < cart.length; i++) {
    grandTotal += cart[i].totalPrice;
}

// Step 3: Membership discount
let membershipType = prompt("Enter membership type (None/Silver/Gold/Platinum)");
let discountRate = 0;

if (membershipType === "Silver") {
    discountRate = 0.05;
} else if (membershipType === "Gold") {
    discountRate = 0.10;
} else if (membershipType === "Platinum") {
    discountRate = 0.15;
}

let discountAmount = grandTotal * discountRate;
let discountedTotal = grandTotal - discountAmount;

// Step 4: GST and platform fee
let gstAmount = discountedTotal * 0.18;
let platformFee = discountedTotal * 0.002;
let totalWithTax = discountedTotal + gstAmount + platformFee;

// Step 5: Payment charges
let paymentMode = prompt("Enter payment mode (Card/UPI/Cash)");
let surcharge = 0;
let convenienceFee = 0;

if (paymentMode === "Card" && totalWithTax < 1000) {
    surcharge = totalWithTax * 0.025;
} else {
    convenienceFee = totalWithTax * 0.01;
}

let finalAmount = totalWithTax + surcharge + convenienceFee;

// Step 6: Invoice details
let invoiceNumber = "INV" + Math.floor(Math.random() * 100000);
let invoiceDate = new Date();

// Step 7: Print invoice
console.log("========= FINAL INVOICE =========");
console.log("Invoice Number:", invoiceNumber);
console.log("Invoice Date:", invoiceDate.toLocaleString());

console.log("----- Item Details -----");
for (let i = 0; i < cart.length; i++) {
    console.log(
        cart[i].itemCode + " | " +
        cart[i].description + " | Qty: " +
        cart[i].quantity + " | Total: " +
        cart[i].totalPrice
    );
}

console.log("-------------------------");
console.log("Subtotal:", grandTotal);
console.log("Discount:", discountAmount);
console.log("GST:", gstAmount);
console.log("Platform Fee:", platformFee);
console.log("Payment Mode:", paymentMode);
console.log("Surcharge:", surcharge);
console.log("Convenience Fee:", convenienceFee);
console.log("Final Amount Payable:", finalAmount);

console.log("Payment Successful");
console.log("Invoice Generated");
