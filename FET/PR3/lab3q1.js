var name = prompt("Please enter your name:");
var age = prompt("Please enter your age:");

age = parseInt(age);

if (isNaN(age)) {
  alert("Please enter a valid age");
} else if (age < 18) {
  alert("You are not eligible to vote.");
} else {
  var confirmAge = confirm("You entered " + age + " as your age. Is this correct?");
  
  if (confirmAge) {
    alert("You are eligible to vote!");
  } else {
    alert("Please enter your correct age.");
  }
}


