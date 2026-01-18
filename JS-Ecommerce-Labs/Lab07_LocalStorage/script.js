// Lab 7: Saving and Retrieving Cart Data using LocalStorage

let cartItems = [
    { itemName: "Notebook", price: 100 },
    { itemName: "Bag", price: 900 }
];

// Save to localStorage
localStorage.setItem("cartData", JSON.stringify(cartItems));
console.log("Cart data saved to localStorage");

// Retrieve from localStorage
let storedData = localStorage.getItem("cartData");

if (storedData) {
    let retrievedCart = JSON.parse(storedData);
    console.log("Retrieved Cart Data:");
    console.log(retrievedCart);
} else {
    console.log("No cart data found");
}
