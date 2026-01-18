// Lab 1: Add Items to Cart

let cart = [];
let grandTotal = 0;
let addMore = true;

while (addMore) {
    let itemCode = prompt("Enter item code:");
    let description = prompt("Enter item description:");
    let quantity = Number(prompt("Enter quantity:"));
    let pricePerUnit = Number(prompt("Enter price per unit:"));

    let totalPrice = quantity * pricePerUnit;

    let item = {
        itemCode: itemCode,
        description: description,
        quantity: quantity,
        pricePerUnit: pricePerUnit,
        totalPrice: totalPrice
    };

    cart.push(item);

    let choice = prompt("Do you want to add another item? (yes/no)");
    if (choice.toLowerCase() !== "yes") {
        addMore = false;
    }
}

// Calculate grand total
for (let i = 0; i < cart.length; i++) {
    grandTotal += cart[i].totalPrice;
}

// Display cart details
console.log("Cart Items:");
for (let i = 0; i < cart.length; i++) {
    console.log(
        cart[i].itemCode + " | " +
        cart[i].description + " | Qty: " +
        cart[i].quantity + " | Total: " +
        cart[i].totalPrice
    );
}

console.log("Grand Total:", grandTotal);
