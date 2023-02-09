// processPayment.js
export function processPayment() {
  const amount = parseFloat(prompt("Enter the payment amount:"));

  if (amount > 0) {
    alert(`Your payment of $${amount} is successful!`);
    return true;
  } else {
    alert("Invalid amount. Please enter a value greater than 0.");
    return processPayment();
  }
}

