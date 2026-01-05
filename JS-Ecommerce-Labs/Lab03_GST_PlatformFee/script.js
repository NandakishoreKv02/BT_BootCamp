// Lab 3: Add GST and Platform Fee

let cart = [];
let grandTotal = 0;
let addMore = true;

// Taking cart items
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

console.log("Grand Total:", grandTotal);

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

console.log("Discount Amount:", discountAmount);
console.log("Total after Discount:", discountedTotal);

// GST and Platform Fee
let gstRate = 0.18;
let platformFeeRate = 0.002;

let gstAmount = discountedTotal * gstRate;
let platformFee = discountedTotal * platformFeeRate;

let totalWithTax = discountedTotal + gstAmount + platformFee;

console.log("GST Amount:", gstAmount);
console.log("Platform Fee:", platformFee);
console.log("Total after Tax and Fees:", totalWithTax);
