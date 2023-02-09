//main.js
import { validateLogin } from './validation.js';
import { processPayment } from './processPayment.js';
import { calculateRating } from './calculateRating.js';

const loginSuccessful = validateLogin();
if (loginSuccessful) {
  const paymentSuccessful = processPayment();
  console.log(`Payment successful: ${paymentSuccessful}`);

  calculateRating();
}
