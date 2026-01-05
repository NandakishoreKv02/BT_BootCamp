// Lab 8: Email Validation using Regex

let email = prompt("Enter your email address:");

let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$/;

if (emailPattern.test(email)) {
    console.log("Valid email address:", email);
    console.log("Thank you message sent");
} else {
    console.log("Invalid email format. Please try again.");
}
