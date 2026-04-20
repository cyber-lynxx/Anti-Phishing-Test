let excerpt1 = "";
let excerpt2 = "";
let excerpt3 = "";
let excerpt4 = "";
let excerpt5 = "";

// The email
fetch("/excerpt1")
  .then(excerpt => excerpt.text())
  .then(str => excerpt1 = str);

// Explanation
fetch("/excerpt2")
  .then(excerpt => excerpt.text())
  .then(str => excerpt2 = str);

// Answer (YES/NO)
fetch("/excerpt3")
  .then(excerpt => excerpt.text())
  .then(str => excerpt3 = str);

// Subject
fetch("/excerpt4")
      .then(excerpt => excerpt.text())
      .then(str => excerpt4 = str);

// Email Address
fetch("/excerpt5")
      .then(excerpt => excerpt.text())
      .then(str => excerpt5 = str);

// "printing" the excerpts onto the HTML
const subjectElement = document.getElementById("subject");
subjectElement.textContent = excerpt4;

const email_addressElement = document.getElementById("email_address");
email_addressElement.textContent = excerpt5;

const emailElement = document.getElementById("email");
emailElement.textContent = excerpt1;

// Checking the user's answer
const yesButton = document.getElementById("yesbutton");
yesButton.addEventListener("click", () => {
  const result = yesButton.value === excerpt3.trim() ? "correct" : "incorrect";

  sessionStorage.setItem("explanation", excerpt2);
  
  window.location.href = `results?answer=${result}`;
});

const noButton = document.getElementById("nobutton");
noButton.addEventListener("click", () => {
  const result = noButton.value === excerpt3.trim() ? "correct" : "incorrect";

  sessionStorage.setItem("explanation", excerpt2);
  
  window.location.href = `results?answer=${result}`;
});
