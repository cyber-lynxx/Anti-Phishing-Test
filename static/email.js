async function loadEmail() {
  try {
    const response = await fetch("https://anti-phishing-test.onrender.com/text");

    // optional but good practice
    if (!response.ok) throw new Error(`HTTP error: ${response.status}`);

    const text = await response.text();

    // now it's safe to update the DOM
    document.getElementById("output").textContent = text;
  } catch (err) {
    console.error("Failed to load email:", err);
    document.getElementById("output").textContent = "Could not load content.";
  }
}

loadEmail();
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
