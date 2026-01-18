// Lab 12: Inventory Lookup using Promises

function checkInventory(itemCode, requiredQty) {
    return new Promise((resolve, reject) => {
        let availableQty = 10;

        if (requiredQty <= availableQty) {
            resolve("Item " + itemCode + " is available");
        } else {
            reject("Insufficient stock for item " + itemCode);
        }
    });
}

let itemCode = prompt("Enter item code:");
let quantity = Number(prompt("Enter quantity:"));

checkInventory(itemCode, quantity)
    .then(message => console.log(message))
    .catch(error => console.log(error));
