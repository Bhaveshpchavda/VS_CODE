// calculateRating.js
export function calculateRating() {
  const rating = parseInt(prompt("Please enter a rating out of 10:"));
  
  if (rating > 6) {
    alert(`Thank you for rating us ${rating}`);
  } else if (rating < 5) {
    alert("Thank you for your feedback. We will try to improve.");
  }
}

