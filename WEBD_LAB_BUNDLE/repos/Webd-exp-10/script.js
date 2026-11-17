const messageButton = document.getElementById("messageButton");
const message = document.getElementById("message");

messageButton.addEventListener("click", function () {
  message.textContent = "Hello! Your static website is working.";
});
