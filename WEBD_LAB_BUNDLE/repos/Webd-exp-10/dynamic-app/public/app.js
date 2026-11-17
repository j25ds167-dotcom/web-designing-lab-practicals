const feedbackForm = document.getElementById("feedbackForm");
const result = document.getElementById("result");

feedbackForm.addEventListener("submit", async function (event) {
  event.preventDefault();

  const formData = {
    name: document.getElementById("name").value,
    message: document.getElementById("message").value
  };

  try {
    const response = await fetch("/feedback", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData)
    });

    const data = await response.json();

    if (!response.ok) {
      result.textContent = data.message;
      return;
    }

    result.textContent = data.message;
    feedbackForm.reset();
  } catch (error) {
    result.textContent = "Could not contact the server. Please try again.";
  }
});
