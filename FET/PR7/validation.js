// validation.js 
export function validateLogin() {
  const username = "admin";
  const password = "password";

  const enteredUsername = prompt("Enter your username:");
  const enteredPassword = prompt("Enter your password:");

  if (enteredUsername === username && enteredPassword === password) {
    alert("Login successful!");
    return true;
  } else {
    alert("Invalid username or password. Please try again.");
    return validateLogin();
  }
}
