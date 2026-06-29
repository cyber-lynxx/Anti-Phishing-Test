async function loadEmail() {
  try {
    const response_str = await fetch("https://anti-phishing-test.onrender.com/text");
    const response_str2 = await response_str.text()
    const response = JSON.parse(response_str2.replace(/'/g, '"'));

    // Stops the program and throws an error if the server responds with any non success code
    if (!response.ok) throw new Error(`HTTP error: ${response.status}`);

    const text = await response.text();

    // Updating the DOM
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
