// Lab 4: Apply Payment Mode Charges

let cart = [];
let grandTotal = 0;
let addMore = true;

// Cart input
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

// Calculate grand total
for (let i = 0; i < cart.length; i++) {
    grandTotal += cart[i].totalPrice;
}

// Membership discount
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

// GST & platform fee
let gstAmount = discountedTotal * 0.18;
let platformFee = discountedTotal * 0.002;

let totalWithTax = discountedTotal + gstAmount + platformFee;

// Payment mode charges
let paymentMode = prompt("Enter payment mode (Card/UPI/Cash)");
let surcharge = 0;
let convenienceFee = 0;

if (paymentMode === "Card" && totalWithTax < 1000) {
    surcharge = totalWithTax * 0.025;
} else {
    convenienceFee = totalWithTax * 0.01;
}

let finalTotal = totalWithTax + surcharge + convenienceFee;

// Display result
console.log("Total after Discount:", discountedTotal);
console.log("GST:", gstAmount);
console.log("Platform Fee:", platformFee);
console.log("Payment Mode:", paymentMode);
console.log("Surcharge:", surcharge);
console.log("Convenience Fee:", convenienceFee);
console.log("Final Total Amount:", finalTotal);
