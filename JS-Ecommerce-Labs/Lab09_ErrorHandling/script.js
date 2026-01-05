// Lab 9: Error Handling and Custom Exceptions

function ValidationError(message) {
    this.name = "ValidationError";
    this.message = message;
}

try {
    let quantity = Number(prompt("Enter quantity:"));
    let price = Number(prompt("Enter price:"));

    if (quantity <= 0) {
        throw new ValidationError("Quantity must be greater than zero");
    }

    if (price <= 0) {
        throw new ValidationError("Price must be greater than zero");
    }

    let total = quantity * price;
    console.log("Total Price:", total);

} catch (error) {
    console.log(error.name + " - " + error.message);
} finally {
    console.log("Validation process completed");
}
