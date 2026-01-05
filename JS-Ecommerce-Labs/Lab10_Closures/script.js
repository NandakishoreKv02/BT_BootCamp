// Lab 10: Closures for Membership Offers

function getDiscountFunction(membershipType) {
    let discountRate = 0;

    if (membershipType === "Silver") {
        discountRate = 0.05;
    } else if (membershipType === "Gold") {
        discountRate = 0.10;
    } else if (membershipType === "Platinum") {
        discountRate = 0.15;
    }

    // Closure function
    return function (amount) {
        return amount * discountRate;
    };
}

let membership = prompt("Enter membership type (Silver/Gold/Platinum)");
let discountCalculator = getDiscountFunction(membership);

let billAmount = Number(prompt("Enter bill amount:"));
let discount = discountCalculator(billAmount);

console.log("Discount Amount:", discount);
console.log("Final Amount:", billAmount - discount);
