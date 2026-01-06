// Lab 11: Asynchronous Payment Processing

async function processPayment(paymentMode) {
    console.log("Processing payment...");

    await new Promise(resolve => setTimeout(resolve, 2000));

    return "Payment Successful using " + paymentMode;
}

async function makePayment() {
    let mode = prompt("Enter payment mode:");
    let result = await processPayment(mode);
    console.log(result);
}

makePayment();
