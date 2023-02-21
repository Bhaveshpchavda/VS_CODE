// register.js
function validateForm() {
    var name = document.forms["registerForm"]["name"].value;
    var email = document.forms["registerForm"]["email"].value;
    var mobile = document.forms["registerForm"]["mobile"].value;
    var password = document.forms["registerForm"]["password"].value;
    var confirmPassword = document.forms["registerForm"]["confirmPassword"].value;
    var errorMessage = "";
  
    if (!name.match(/^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/)) {
      errorMessage += "Name is invalid\n";
    }
  
    if (!email.match(/^\S+@\S+\.\S+$/)) {
      errorMessage += "Email is invalid\n";
    }
  
    if (!mobile.match(/^(\+\d{1,3}[- ]?)?\d{10}$/)) {
      errorMessage += "Mobile number is invalid\n";
    }
  
    if (password.length < 8) {
      errorMessage += "Password must be at least 8 characters long\n";
    }
  
    if (!password.match(/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/)) {
      errorMessage += "Password must contain at least one letter and one number\n";
    }
  
    if (password != confirmPassword) {
      errorMessage += "Passwords do not match\n";
    }
  
    if (errorMessage != "") {
      alert(errorMessage);
      return false;
    }
  }
  