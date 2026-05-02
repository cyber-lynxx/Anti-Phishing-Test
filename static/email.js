let text = "";

// The email
fetch("https://anti-phishing-test.onrender.com/text")
  .then(output => output.text())
  .then(str => text = str);

//"printing" the excerpts onto the HTML
const subjectElement = document.getElementById("output");
subjectElement.textContent = text;

// Checking the user's answer
//const yesButton = document.getElementById("yesbutton");
//yesButton.addEventListener("click", () => {
  //const result = yesButton.value === excerpt3.trim() ? "correct" : "incorrect";

  //sessionStorage.setItem("explanation", excerpt2);
  //sessionStorage.setItem("user_answer", yesButton.value);
  
  //window.location.href = `results?answer=${result}`;
//});

//const noButton = document.getElementById("nobutton");
//noButton.addEventListener("click", () => {
  //const result = noButton.value === excerpt3.trim() ? "correct" : "incorrect";

  //sessionStorage.setItem("explanation", excerpt2);
  //sessionStorage.setItem("user_answer", noButton.value);
  
  //window.location.href = `results?answer=${result}`;
//});
