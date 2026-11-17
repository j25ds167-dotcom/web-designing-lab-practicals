const express = require("express");
const path = require("path");

const app = express();

// Read form data sent by the browser
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Show the HTML page from the public folder
app.use(express.static(path.join(__dirname, "public")));

// Store submitted messages while the server is running
// This simple array resets whenever the server restarts.
let feedbackList = [];

// Home route
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

// Health route for checking whether the server is running
app.get("/health", (req, res) => {
  res.json({
    status: "OK",
    message: "Dynamic Node.js application is running."
  });
});

// Receive a feedback message from the form
app.post("/feedback", (req, res) => {
  const name = String(req.body.name || "").trim();
  const message = String(req.body.message || "").trim();

  if (!name || !message) {
    return res.status(400).json({
      success: false,
      message: "Please enter your name and feedback."
    });
  }

  const feedback = {
    id: feedbackList.length + 1,
    name: name,
    message: message
  };

  feedbackList.push(feedback);

  res.json({
    success: true,
    message: "Thank you! Your feedback was received.",
    feedback: feedback
  });
});

// Display all submitted feedback
app.get("/feedback", (req, res) => {
  res.json(feedbackList);
});

// Use the port provided by the hosting service
const PORT = process.env.PORT || 3000;

app.listen(PORT, "0.0.0.0", () => {
  console.log("Dynamic app is running on port " + PORT);
});
