const headings = document.querySelectorAll(".heading");

for (let heading of headings) {
  heading.addEventListener("click", function() {
    let content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      for (let otherHeading of headings) {
        let otherContent = otherHeading.nextElementSibling;
        otherContent.style.display = "none";
      }
      content.style.display = "block";
    }
  });
}
