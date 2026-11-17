EXP7 = dict(
    n=7,
    title="Develop a single-page React application for managing notes (CRUD operations).",
    aim="To develop a React single-page application that allows users to create, view, update, and delete notes.",
    desc="React is a JavaScript library for building component-based user interfaces. Components divide an application into reusable parts. State stores data that can change over time; useState is commonly used for local component state. CRUD refers to Create, Read, Update, and Delete operations. React re-renders the interface when state changes.",
    software=["Node.js", "VS Code", "Web browser"],
    files=[("src/App.jsx", r'''import { useState } from "react";
import "./App.css";

function App() {
  const [notes, setNotes] = useState([]);
  const [text, setText] = useState("");
  const [editId, setEditId] = useState(null);

  function saveNote() {
    if (text.trim() === "") {
      alert("Please write a note");
      return;
    }

    if (editId === null) {
      setNotes([...notes, { id: Date.now(), text: text }]);
    } else {
      setNotes(notes.map(note =>
        note.id === editId ? { ...note, text: text } : note
      ));
      setEditId(null);
    }
    setText("");
  }

  function editNote(note) {
    setText(note.text);
    setEditId(note.id);
  }

  function deleteNote(id) {
    setNotes(notes.filter(note => note.id !== id));
  }

  return (
    <div className="app">
      <h1>My Notes</h1>
      <textarea
        value={text}
        onChange={event => setText(event.target.value)}
        placeholder="Write your note"
      />
      <br />
      <button onClick={saveNote}>
        {editId === null ? "Add Note" : "Update Note"}
      </button>

      {notes.map(note => (
        <div className="note" key={note.id}>
          <p>{note.text}</p>
          <button onClick={() => editNote(note)}>Edit</button>
          <button onClick={() => deleteNote(note.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
}

export default App;
'''), ("src/App.css", r'''body {
  font-family: Arial;
  background: #f2f2f2;
}
.app {
  width: 80%;
  max-width: 600px;
  margin: 30px auto;
  text-align: center;
}
textarea {
  width: 90%;
  height: 80px;
  padding: 10px;
}
button {
  padding: 8px 12px;
  margin: 5px;
  cursor: pointer;
}
.note {
  background: white;
  padding: 10px;
  margin-top: 12px;
  text-align: left;
  border-radius: 5px;
}
'''), ("src/main.jsx", r'''import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
'''), ("index.html", r'''<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>React Notes</title>
</head>
<body>
  <div id="root"></div>
  <script type="module" src="/src/main.jsx"></script>
</body>
</html>
'''), ("package.json", r'''{
  "name": "react-notes",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.3.4",
    "vite": "^5.4.11"
  }
}
'''), ("vite.config.js", r'''import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  base: "./",
  plugins: [react()]
});
'''), (".gitignore", "node_modules\ndist\n.env\n")],
    output="A React single-page application where users can add, view, update, and delete notes.",
    shots=["Notes app with a note added", "GitHub repository"],
    live=True,
    pages_build=True,
    conclusion="In this experiment I developed a notes application with React. I learned about components, state with useState, event handling and rendering lists, and I used them to build the create, read, update and delete operations.",
)

EXP8 = dict(
    n=8,
    title="Build a RESTful API using Node.js and Express.js for a book collection.",
    aim="To create a RESTful API using Node.js and Express.js that performs CRUD operations on a book collection.",
    desc="Node.js allows JavaScript to run outside the browser. Express.js is a lightweight framework for creating HTTP servers and routes. A RESTful API exposes resources through URLs and HTTP methods. GET retrieves data, POST creates data, PUT or PATCH updates data, and DELETE removes data. JSON is commonly used for request and response bodies.",
    software=["Node.js", "VS Code", "Postman or a web browser"],
    files=[("server.js", r'''const express = require("express");
const app = express();

app.use(express.json());

// Temporary book data
let books = [
  { id: 1, title: "Wings of Fire", author: "A. P. J. Abdul Kalam" },
  { id: 2, title: "The Alchemist", author: "Paulo Coelho" }
];

// GET: Display all books
app.get("/books", (req, res) => {
  res.json(books);
});

// GET: Display one book
app.get("/books/:id", (req, res) => {
  const book = books.find(b => b.id === Number(req.params.id));
  if (!book) return res.status(404).send("Book not found");
  res.json(book);
});

// POST: Add a new book
app.post("/books", (req, res) => {
  const newBook = {
    id: Date.now(),
    title: req.body.title,
    author: req.body.author
  };
  books.push(newBook);
  res.status(201).json(newBook);
});

// PUT: Update a book
app.put("/books/:id", (req, res) => {
  const book = books.find(b => b.id === Number(req.params.id));
  if (!book) return res.status(404).send("Book not found");

  book.title = req.body.title || book.title;
  book.author = req.body.author || book.author;
  res.json(book);
});

// DELETE: Remove a book
app.delete("/books/:id", (req, res) => {
  const oldLength = books.length;
  books = books.filter(b => b.id !== Number(req.params.id));

  if (books.length === oldLength) {
    return res.status(404).send("Book not found");
  }
  res.send("Book deleted successfully");
});

app.listen(3000, () => {
  console.log("Server running at http://localhost:3000");
});
'''), ("package.json", r'''{
  "name": "book-api",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": { "start": "node server.js" },
  "dependencies": { "express": "^4.21.2" }
}
'''), ("requests.http", r'''### Get all books
GET http://localhost:3000/books

### Get one book
GET http://localhost:3000/books/1

### Add a book
POST http://localhost:3000/books
Content-Type: application/json

{ "title": "Atomic Habits", "author": "James Clear" }

### Update a book
PUT http://localhost:3000/books/1
Content-Type: application/json

{ "title": "Wings of Fire (Updated)" }

### Delete a book
DELETE http://localhost:3000/books/2
'''), (".gitignore", "node_modules\n.env\n")],
    output="A REST API that supports GET, POST, PUT, and DELETE operations for a book collection. The data is stored temporarily in memory and resets when the server restarts.",
    shots=["Browser/Postman output of GET /books", "GitHub repository"],
    live=False,
    live_note="Not applicable. A Node.js API needs a running server, which GitHub Pages cannot provide. The API is run locally at http://localhost:3000.",
    conclusion="In this experiment I created a RESTful API with Node.js and Express.js. I learned how the HTTP methods GET, POST, PUT and DELETE map to read, create, update and delete operations, and how to test the routes using Postman or the browser.",
)

EXP9 = dict(
    n=9,
    title="Implement user authentication using Node.js, Express.js, MongoDB, and JWT.",
    aim="To implement secure user registration and login/logout functionality using Node.js, Express.js, MongoDB, password hashing, and JSON Web Tokens (JWT).",
    desc="Authentication verifies a user's identity. MongoDB stores user records, while Express routes handle registration and login requests. Passwords must be hashed using a password-hashing library such as bcrypt; plain-text passwords must never be stored. After successful login, the server can issue a signed JWT. Protected routes verify the token before returning private data. The .env file holds secrets and must never be committed to GitHub; only .env.example is committed.",
    software=["Node.js", "VS Code", "MongoDB Community Server or MongoDB Atlas", "Postman"],
    files=[("server.js", r'''require("dotenv").config();

const express = require("express");
const mongoose = require("mongoose");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const path = require("path");

const app = express();

app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

// Check environment settings
if (!process.env.MONGO_URI || !process.env.JWT_SECRET) {
  console.error("Please configure MONGO_URI and JWT_SECRET in the .env file.");
  process.exit(1);
}

// User model: unique email and hashed password
const userSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    trim: true
  },
  passwordHash: {
    type: String,
    required: true
  }
});

const User = mongoose.model("User", userSchema);

// Home page
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

// POST /register
app.post("/register", async (req, res) => {
  try {
    const email = String(req.body.email || "").trim().toLowerCase();
    const password = String(req.body.password || "");

    if (!email || !password) {
      return res.status(400).json({ message: "Email and password are required." });
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
      return res.status(400).json({ message: "Please enter a valid email address." });
    }

    if (password.length < 8) {
      return res.status(400).json({ message: "Password must be at least 8 characters long." });
    }

    const existingUser = await User.findOne({ email: email });
    if (existingUser) {
      return res.status(409).json({ message: "This email is already registered. Please log in." });
    }

    // Hash password before storing it
    const passwordHash = await bcrypt.hash(password, 10);

    const user = new User({ email: email, passwordHash: passwordHash });
    await user.save();

    return res.status(201).json({ message: "Registration successful. You can now log in." });
  } catch (error) {
    if (error.code === 11000) {
      return res.status(409).json({ message: "This email is already registered." });
    }
    console.error("Register error:", error.message);
    return res.status(500).json({ message: "Server error during registration." });
  }
});

// POST /login
app.post("/login", async (req, res) => {
  try {
    const email = String(req.body.email || "").trim().toLowerCase();
    const password = String(req.body.password || "");

    if (!email || !password) {
      return res.status(400).json({ message: "Email and password are required." });
    }

    const user = await User.findOne({ email: email });
    if (!user) {
      return res.status(401).json({ message: "Invalid email or password." });
    }

    // Compare entered password with saved password hash
    const passwordMatches = await bcrypt.compare(password, user.passwordHash);
    if (!passwordMatches) {
      return res.status(401).json({ message: "Invalid email or password." });
    }

    // Create a signed JWT with one-hour expiry
    const token = jwt.sign(
      { userId: user._id.toString() },
      process.env.JWT_SECRET,
      { expiresIn: "1h" }
    );

    return res.json({
      message: "Login successful.",
      token: token,
      tokenType: "Bearer",
      expiresIn: "1h"
    });
  } catch (error) {
    console.error("Login error:", error.message);
    return res.status(500).json({ message: "Server error during login." });
  }
});

// JWT authentication middleware
function authenticateToken(req, res, next) {
  const authHeader = req.headers.authorization;

  if (!authHeader || !authHeader.startsWith("Bearer ")) {
    return res.status(401).json({ message: "Access denied. Please log in first." });
  }

  const token = authHeader.split(" ")[1];

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.userId = decoded.userId;
    next();
  } catch (error) {
    return res.status(401).json({ message: "Invalid or expired token. Please log in again." });
  }
}

// Protected profile route
app.get("/profile", authenticateToken, async (req, res) => {
  try {
    const user = await User.findById(req.userId).select("-passwordHash");

    if (!user) {
      return res.status(404).json({ message: "User not found." });
    }

    return res.json({
      message: "You are viewing a protected profile.",
      email: user.email
    });
  } catch (error) {
    console.error("Profile error:", error.message);
    return res.status(500).json({ message: "Could not load profile." });
  }
});

// Logout for the stateless Bearer-token approach
app.post("/logout", (req, res) => {
  return res.json({ message: "Logged out. Remove the token from client storage." });
});

// A stateless JWT is not automatically invalidated on the server
// when the client deletes it. It remains valid until expiry unless
// a server-side token revocation strategy is implemented.

const PORT = process.env.PORT || 3000;

mongoose.connect(process.env.MONGO_URI)
  .then(() => {
    console.log("MongoDB connected successfully.");
    app.listen(PORT, () => {
      console.log("Server running at http://localhost:" + PORT);
    });
  })
  .catch((error) => {
    console.error("MongoDB connection failed:", error.message);
    process.exit(1);
  });
'''), ("public/index.html", r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>User Authentication</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main class="page">
    <header class="page-heading">
      <span class="small-label">WEB DESIGNING LAB &middot; EXPERIMENT 9</span>
      <h1>User Authentication</h1>
      <p>Create an account or log in securely.</p>
    </header>

    <section class="auth-container" id="authContainer">
      <!-- Registration Card -->
      <div class="auth-card">
        <div class="card-heading">
          <span class="icon">&#10010;</span>
          <h2>Register</h2>
        </div>
        <form id="registerForm">
          <label for="registerEmail">Username / Email</label>
          <input type="email" id="registerEmail" placeholder="Enter your email" autocomplete="username" required>

          <label for="registerPassword">Password</label>
          <input type="password" id="registerPassword" placeholder="Create a password (minimum 8 characters)" autocomplete="new-password" minlength="8" required>

          <button type="submit">Register</button>
          <p class="switch-text">Already have an account? <a href="#" id="showLogin">Login</a></p>
        </form>
        <p class="message" id="registerMessage" aria-live="polite"></p>
      </div>

      <!-- Login Card -->
      <div class="auth-card">
        <div class="card-heading">
          <span class="icon">&#9679;</span>
          <h2>Login</h2>
        </div>
        <form id="loginForm">
          <label for="loginEmail">Username / Email</label>
          <input type="email" id="loginEmail" placeholder="Enter your email" autocomplete="username" required>

          <label for="loginPassword">Password</label>
          <input type="password" id="loginPassword" placeholder="Enter your password" autocomplete="current-password" required>

          <button type="submit">Login</button>
          <p class="switch-text">Don't have an account? <a href="#" id="showRegister">Register</a></p>
        </form>
        <p class="message" id="loginMessage" aria-live="polite"></p>
      </div>
    </section>

    <!-- Protected Profile -->
    <section class="profile-card hidden" id="profileCard">
      <div class="card-heading">
        <span class="icon">&#10003;</span>
        <h2>Welcome</h2>
      </div>
      <p id="profileEmail"></p>
      <p class="profile-note">You have accessed a JWT-protected route.</p>
      <button id="logoutButton" class="logout-button">Logout</button>
      <p class="message" id="profileMessage" aria-live="polite"></p>
    </section>

    <footer>Node.js &middot; Express.js &middot; MongoDB &middot; bcrypt &middot; JSON Web Token</footer>
  </main>

  <script src="app.js"></script>
</body>
</html>
'''), ("public/style.css", r'''* {
  box-sizing: border-box;
}
body {
  margin: 0;
  min-height: 100vh;
  font-family: Arial, Helvetica, sans-serif;
  color: #172033;
  background: linear-gradient(135deg, #eef5ff, #f8fbff 55%, #edf2ff);
}
.page {
  width: min(1100px, 92%);
  margin: 0 auto;
  padding: 52px 0 30px;
}
.page-heading {
  text-align: center;
  margin-bottom: 30px;
}
.small-label {
  color: #1769e8;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 1.5px;
}
.page-heading h1 {
  margin: 10px 0 8px;
  font-size: clamp(28px, 4vw, 38px);
}
.page-heading p {
  color: #64748b;
  margin: 0;
}
.auth-container {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 30px;
}
.auth-card,
.profile-card {
  background: #ffffff;
  border: 1px solid #e5eaf2;
  border-radius: 14px;
  padding: 28px 30px;
  box-shadow: 0 12px 35px rgba(36, 70, 120, 0.10);
}
.card-heading {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 13px;
  border-bottom: 1px solid #e8edf5;
  padding-bottom: 17px;
  margin-bottom: 22px;
}
.card-heading h2 {
  margin: 0;
  font-size: 25px;
}
.icon {
  display: inline-flex;
  width: 34px;
  height: 34px;
  align-items: center;
  justify-content: center;
  color: white;
  background: #1670ee;
  border-radius: 50%;
  font-weight: 700;
}
form {
  display: flex;
  flex-direction: column;
}
label {
  margin: 0 0 8px;
  font-size: 15px;
  font-weight: 700;
  color: #475569;
}
input {
  width: 100%;
  padding: 13px 14px;
  margin-bottom: 20px;
  border: 1px solid #cbd5e1;
  border-radius: 7px;
  outline: none;
  font-size: 15px;
  background: #fbfdff;
}
input:focus {
  border-color: #1670ee;
  box-shadow: 0 0 0 3px rgba(22, 112, 238, 0.12);
}
button {
  border: 0;
  border-radius: 7px;
  padding: 13px 16px;
  color: white;
  background: #1670ee;
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s;
}
button:hover {
  background: #0758c9;
}
.switch-text {
  margin: 20px 0 0;
  text-align: center;
  color: #64748b;
  font-size: 14px;
}
a {
  color: #1269e8;
  font-weight: 700;
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
.message {
  min-height: 20px;
  margin: 14px 0 0;
  text-align: center;
  font-size: 14px;
  color: #176b39;
}
.message.error {
  color: #c62828;
}
.profile-card {
  max-width: 520px;
  margin: 0 auto;
  text-align: center;
}
.profile-note {
  color: #64748b;
}
.logout-button {
  margin-top: 12px;
  background: #dc3545;
}
.logout-button:hover {
  background: #b92534;
}
.hidden {
  display: none;
}
footer {
  margin-top: 30px;
  text-align: center;
  color: #8491a5;
  font-size: 13px;
}
@media (max-width: 720px) {
  .page {
    padding-top: 30px;
  }
  .auth-container {
    grid-template-columns: 1fr;
    gap: 18px;
  }
  .auth-card {
    padding: 24px 20px;
  }
}
'''), ("public/app.js", r'''const registerForm = document.getElementById("registerForm");
const loginForm = document.getElementById("loginForm");
const registerMessage = document.getElementById("registerMessage");
const loginMessage = document.getElementById("loginMessage");
const authContainer = document.getElementById("authContainer");
const profileCard = document.getElementById("profileCard");
const profileEmail = document.getElementById("profileEmail");
const profileMessage = document.getElementById("profileMessage");

// Display success or error messages
function showMessage(element, message, isError = false) {
  element.textContent = message;
  element.classList.toggle("error", isError);
}

// Register a new user
registerForm.addEventListener("submit", async function (event) {
  event.preventDefault();

  const email = document.getElementById("registerEmail").value;
  const password = document.getElementById("registerPassword").value;

  showMessage(registerMessage, "Creating your account...");

  try {
    const response = await fetch("/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email, password: password })
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message || "Registration failed.");
    }

    showMessage(registerMessage, data.message);
    registerForm.reset();

    // Fill the login email field after successful registration
    document.getElementById("loginEmail").value = email;
  } catch (error) {
    showMessage(registerMessage, error.message, true);
  }
});

// Login an existing user
loginForm.addEventListener("submit", async function (event) {
  event.preventDefault();

  const email = document.getElementById("loginEmail").value;
  const password = document.getElementById("loginPassword").value;

  showMessage(loginMessage, "Logging in...");

  try {
    const response = await fetch("/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email, password: password })
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message || "Login failed.");
    }

    // Store JWT for this browser tab
    sessionStorage.setItem("authToken", data.token);
    loginForm.reset();
    showMessage(loginMessage, "");
    await loadProfile();
  } catch (error) {
    showMessage(loginMessage, error.message, true);
  }
});

// Access the protected profile using the JWT
async function loadProfile() {
  const token = sessionStorage.getItem("authToken");
  if (!token) {
    return;
  }

  try {
    const response = await fetch("/profile", {
      method: "GET",
      headers: { "Authorization": "Bearer " + token }
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message || "Could not load profile.");
    }

    profileEmail.textContent = "Logged in as: " + data.email;
    authContainer.classList.add("hidden");
    profileCard.classList.remove("hidden");
  } catch (error) {
    sessionStorage.removeItem("authToken");
    showMessage(loginMessage, error.message, true);
  }
}

// Logout by removing the JWT from this browser tab
document.getElementById("logoutButton").addEventListener("click", async function () {
  const token = sessionStorage.getItem("authToken");

  try {
    await fetch("/logout", {
      method: "POST",
      headers: token ? { "Authorization": "Bearer " + token } : {}
    });
  } catch (error) {
    // Remove the local token even if the logout request fails
  }

  sessionStorage.removeItem("authToken");
  profileCard.classList.add("hidden");
  authContainer.classList.remove("hidden");
  showMessage(profileMessage, "");
  showMessage(loginMessage, "You have logged out.");
});

// Focus the relevant form when the links are clicked
document.getElementById("showLogin").addEventListener("click", function (event) {
  event.preventDefault();
  document.getElementById("loginEmail").focus();
});

document.getElementById("showRegister").addEventListener("click", function (event) {
  event.preventDefault();
  document.getElementById("registerEmail").focus();
});

// Restore profile after refreshing the page in the same tab
loadProfile();
'''), ("package.json", r'''{
  "name": "experiment-9-user-authentication",
  "version": "1.0.0",
  "description": "User authentication using Node.js, Express, MongoDB, bcrypt and JWT",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "bcrypt": "^5.1.1",
    "dotenv": "^16.4.7",
    "express": "^4.21.2",
    "jsonwebtoken": "^9.0.2",
    "mongoose": "^8.9.5"
  }
}
'''), (".env.example", r'''PORT=3000
MONGO_URI=mongodb://127.0.0.1:27017/experiment9_auth
JWT_SECRET=PASTE_YOUR_GENERATED_RANDOM_SECRET_HERE
'''), (".gitignore", ".env\nnode_modules\n"), ("README.md", r'''# Experiment 9 - User Authentication

1. `npm install`
2. Copy `.env.example` to `.env` and fill in your own values.
   Generate a secret with:
   `node -e "console.log(require('crypto').randomBytes(48).toString('hex'))"`
3. Start MongoDB, then run `npm start` and open http://localhost:3000

Never commit the `.env` file.
''')],
    output="A backend with registration, login, password hashing, JWT token generation, and a protected profile route.",
    shots=["Register and login page", "Welcome page after login (protected route)", "GitHub repository (no .env file)"],
    live=False,
    live_note="Not applicable. This app needs Node.js and MongoDB running on a server, which GitHub Pages cannot provide. It is run locally at http://localhost:3000.",
    conclusion="In this experiment I implemented user authentication with Express.js, MongoDB, bcrypt and JWT. I learned that passwords must be hashed before they are stored, that a signed token can protect private routes, and that secrets belong in a .env file that is kept out of GitHub.",
)

EXP10 = dict(
    n=10,
    title="Deploy a static website on Netlify and a dynamic website on Heroku or AWS.",
    aim="To understand and perform deployment of a static website and a dynamic web application using cloud hosting platforms.",
    desc="Deployment makes a website available over the internet. Static sites contain files such as HTML, CSS, JavaScript, and images and can be hosted through platforms such as Netlify. Dynamic applications execute server-side code and may require runtime configuration, environment variables, and a database. In this repository the static site is in the root folder and the Node.js app is in the dynamic-app folder.",
    software=["A static HTML/CSS/JavaScript website", "GitHub account", "Netlify account", "Node.js for the dynamic example", "An AWS or Heroku (or similar) account"],
    files=[("index.html", r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My First Deployed Website</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="header">
    <h1>My First Website</h1>
    <p>Experiment 10 - Static Website Deployment</p>
  </header>

  <main class="container">
    <section class="card">
      <h2>Welcome!</h2>
      <p>This is a simple static website made using HTML, CSS and JavaScript.</p>
      <button id="messageButton">Click Me</button>
      <p id="message"></p>
    </section>

    <section class="card">
      <h2>About This Experiment</h2>
      <p>This website is uploaded to GitHub and deployed using Netlify.</p>
      <ul>
        <li>HTML creates the webpage structure.</li>
        <li>CSS adds colours and layout.</li>
        <li>JavaScript adds a small interaction.</li>
      </ul>
    </section>
  </main>

  <footer>
    <p>Web Designing Lab | Experiment 10</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>
'''), ("style.css", r'''* {
  box-sizing: border-box;
}
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: #f1f5fb;
  color: #1e293b;
}
.header {
  padding: 35px 15px;
  text-align: center;
  color: white;
  background: #1769e8;
}
.header h1 {
  margin: 0 0 8px;
}
.header p {
  margin: 0;
}
.container {
  width: min(900px, 90%);
  margin: 35px auto;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 22px;
}
.card {
  padding: 25px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 5px 18px rgba(0, 0, 0, 0.08);
}
.card h2 {
  color: #1769e8;
}
button {
  padding: 11px 20px;
  border: 0;
  border-radius: 6px;
  color: white;
  background: #1769e8;
  cursor: pointer;
}
button:hover {
  background: #0d4fb8;
}
#message {
  color: #16803c;
  font-weight: bold;
}
footer {
  padding: 18px;
  text-align: center;
  color: #64748b;
}
@media (max-width: 650px) {
  .container {
    grid-template-columns: 1fr;
  }
}
'''), ("script.js", r'''const messageButton = document.getElementById("messageButton");
const message = document.getElementById("message");

messageButton.addEventListener("click", function () {
  message.textContent = "Hello! Your static website is working.";
});
'''), ("dynamic-app/package.json", r'''{
  "name": "experiment-10-dynamic-app",
  "version": "1.0.0",
  "description": "Beginner Node.js and Express dynamic web application",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "engines": {
    "node": ">=20"
  },
  "dependencies": {
    "express": "^4.21.2"
  }
}
'''), ("dynamic-app/server.js", r'''const express = require("express");
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
'''), ("dynamic-app/public/index.html", r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dynamic Feedback App</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main class="box">
    <h1>Dynamic Feedback App</h1>
    <p class="intro">Experiment 10 - Node.js and Express Deployment</p>

    <form id="feedbackForm">
      <label for="name">Your Name</label>
      <input type="text" id="name" name="name" placeholder="Enter your name" required>

      <label for="message">Your Feedback</label>
      <textarea id="message" name="message" rows="4" placeholder="Write your feedback" required></textarea>

      <button type="submit">Submit Feedback</button>
    </form>

    <p id="result" aria-live="polite"></p>

    <div class="links">
      <a href="/health" target="_blank">Check Server Health</a>
      <a href="/feedback" target="_blank">View Submitted Feedback (JSON)</a>
    </div>
  </main>

  <script src="app.js"></script>
</body>
</html>
'''), ("dynamic-app/public/style.css", r'''* {
  box-sizing: border-box;
}
body {
  margin: 0;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 20px;
  font-family: Arial, sans-serif;
  background: #edf3fb;
  color: #1e293b;
}
.box {
  width: min(520px, 100%);
  padding: 30px;
  border-radius: 12px;
  background: white;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.09);
}
h1 {
  margin-top: 0;
  color: #1769e8;
  text-align: center;
}
.intro {
  text-align: center;
  color: #64748b;
  margin-bottom: 25px;
}
label {
  display: block;
  margin: 15px 0 7px;
  font-weight: bold;
}
input, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  font: inherit;
}
textarea {
  resize: vertical;
}
button {
  width: 100%;
  margin-top: 18px;
  padding: 12px;
  border: 0;
  border-radius: 6px;
  color: white;
  background: #1769e8;
  font-size: 16px;
  cursor: pointer;
}
button:hover {
  background: #0d4fb8;
}
#result {
  min-height: 22px;
  color: #16803c;
  text-align: center;
  font-weight: bold;
}
.links {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 20px;
}
a {
  color: #1769e8;
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
'''), ("dynamic-app/public/app.js", r'''const feedbackForm = document.getElementById("feedbackForm");
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
'''), (".gitignore", "node_modules\n.env\n"), ("README.md", r'''# Experiment 10 - Deployment

- Static site: `index.html`, `style.css`, `script.js` in the root folder
  (GitHub Pages / Netlify publish directory: root).
- Dynamic app: `dynamic-app/` (Node.js + Express).
  Deploy with root directory `dynamic-app`, build command `npm install`,
  start command `npm start`. The host provides the PORT variable.
''')],
    output="A static website published through Netlify (and GitHub Pages) and a dynamic Node.js website deployed on a cloud hosting platform.",
    shots=["Static website", "Dynamic feedback app", "Netlify / hosting dashboard", "GitHub repository"],
    live=True,
    extra_links=[("Netlify URL", "PASTE_YOUR_NETLIFY_URL_HERE"), ("Dynamic app URL (Render/AWS/Heroku)", "PASTE_YOUR_DYNAMIC_APP_URL_HERE")],
    conclusion="In this experiment I learned how a static website and a dynamic website are deployed. I understood the role of GitHub, hosting platforms, start commands, the PORT environment variable, and why a Node.js app needs a server while a static site does not.",
)

EXP11 = dict(
    n=11,
    title="Optimize a website using caching, CSS/JS minification, and lazy loading of images.",
    aim="To improve website loading performance by applying browser caching, minification of CSS and JavaScript, and lazy loading of images.",
    desc="Web performance optimization reduces download size and improves perceived loading speed. Minification removes unnecessary whitespace and comments from CSS and JavaScript. Browser caching allows reusable resources to be stored locally according to HTTP cache headers. Lazy loading delays loading off-screen images until they are near the viewport. Performance should be measured before and after changes using Chrome DevTools or Lighthouse.",
    software=["VS Code", "Google Chrome", "A local web server or hosting platform"],
    files=[("index.html", r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Optimized Website</title>
  <link rel="stylesheet" href="style.min.css">
</head>
<body>
  <h1>Optimized Image Gallery</h1>
  <p>Images below use lazy loading.</p>
  <img src="photo1.jpg" alt="Sunrise gradient" loading="lazy" width="300" height="200">
  <img src="photo2.jpg" alt="Ocean gradient" loading="lazy" width="300" height="200">
  <img src="photo3.jpg" alt="Forest gradient" loading="lazy" width="300" height="200">
  <script src="script.min.js" defer></script>
</body>
</html>
'''), ("style.css", r'''body {
  font-family: Arial;
  text-align: center;
  background: #f4f4f4;
}
img {
  margin: 10px;
  border-radius: 8px;
}
'''), ("style.min.css", "body{font-family:Arial;text-align:center;background:#f4f4f4}img{margin:10px;border-radius:8px}\n"),
           ("script.js", r'''window.addEventListener("load", function () {
  console.log("Optimized webpage loaded");
});
'''), ("script.min.js", 'window.addEventListener("load",function(){console.log("Optimized webpage loaded")});\n'),
           (".htaccess-example.txt", r'''# Example Apache caching rules.
# Use these rules only on an Apache server with mod_expires enabled.
# (GitHub Pages sets its own cache headers and ignores this file.)
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
</IfModule>
''')],
    output="A webpage that uses minified CSS and JavaScript, lazy-loaded images, and an example of browser caching configuration.",
    shots=["Optimized gallery page", "Chrome DevTools Network tab / Lighthouse score", "GitHub repository"],
    live=True,
    conclusion="In this experiment I optimized a webpage using minified CSS and JavaScript, lazy-loaded images with width and height set, and an example caching configuration. I learned how these techniques reduce the amount of data downloaded and improve page loading time.",
)

EXP12 = dict(
    n=12,
    title="Deploy a full-stack MERN application on a cloud platform.",
    aim="To develop and deploy a full-stack MERN application using MongoDB, Express.js, React.js, and Node.js on a cloud platform.",
    desc="MERN is a full-stack JavaScript technology combination. MongoDB stores application data, Express.js and Node.js provide backend APIs, and React.js provides the frontend interface. The frontend communicates with backend endpoints using HTTP requests. A cloud deployment requires separate or combined hosting configuration, environment variables, database network access, and correct API URLs. Secrets must remain on the server and must not be committed to source control.",
    software=["Node.js", "VS Code", "MongoDB Atlas or local MongoDB", "GitHub", "A cloud hosting platform"],
    files=[("backend/server.js", r'''require("dotenv").config();

const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log("MongoDB connected"))
  .catch(error => console.log(error));

const Task = mongoose.model("Task", new mongoose.Schema({
  title: { type: String, required: true }
}));

app.get("/tasks", async (req, res) => {
  const tasks = await Task.find();
  res.json(tasks);
});

app.post("/tasks", async (req, res) => {
  const task = new Task({ title: req.body.title });
  await task.save();
  res.status(201).json(task);
});

app.delete("/tasks/:id", async (req, res) => {
  await Task.findByIdAndDelete(req.params.id);
  res.send("Task deleted");
});

app.get("/", (req, res) => {
  res.send("MERN Task API is running");
});

app.listen(process.env.PORT || 5000, () => {
  console.log("Backend running");
});
'''), ("backend/package.json", r'''{
  "name": "mern-task-backend",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": { "start": "node server.js" },
  "dependencies": {
    "cors": "^2.8.5",
    "dotenv": "^16.4.7",
    "express": "^4.21.2",
    "mongoose": "^8.9.5"
  }
}
'''), ("backend/.env.example", r'''MONGO_URI=mongodb://127.0.0.1:27017/task_app
PORT=5000
'''), ("backend/.gitignore", ".env\nnode_modules\n"),
           ("frontend/package.json", r'''{
  "name": "mern-task-frontend",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.3.4",
    "vite": "^5.4.11"
  }
}
'''), ("frontend/vite.config.js", r'''import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()]
});
'''), ("frontend/.gitignore", "node_modules\ndist\n.env\n"),
           ("frontend/index.html", r'''<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MERN Task App</title>
</head>
<body>
  <div id="root"></div>
  <script type="module" src="/src/main.jsx"></script>
</body>
</html>
'''), ("frontend/src/main.jsx", r'''import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode><App /></React.StrictMode>
);
'''), ("frontend/src/App.jsx", r'''import { useEffect, useState } from "react";

// In production set VITE_API_URL to your deployed backend URL
const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000";

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  async function loadTasks() {
    const response = await fetch(API_URL + "/tasks");
    const data = await response.json();
    setTasks(data);
  }

  async function addTask() {
    if (title.trim() === "") return;

    await fetch(API_URL + "/tasks", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title: title })
    });

    setTitle("");
    loadTasks();
  }

  async function deleteTask(id) {
    await fetch(API_URL + "/tasks/" + id, { method: "DELETE" });
    loadTasks();
  }

  useEffect(() => {
    loadTasks();
  }, []);

  return (
    <div style={{ textAlign: "center", fontFamily: "Arial" }}>
      <h1>MERN Task Manager</h1>

      <input
        value={title}
        onChange={event => setTitle(event.target.value)}
        placeholder="Enter a task"
      />
      <button onClick={addTask}>Add Task</button>

      {tasks.map(task => (
        <p key={task._id}>
          {task.title}
          <button onClick={() => deleteTask(task._id)}>Delete</button>
        </p>
      ))}
    </div>
  );
}

export default App;
'''), ("frontend/.env.example", "VITE_API_URL=http://localhost:5000\n"),
           ("README.md", r'''# Experiment 12 - MERN Task Manager

Backend: `cd backend && npm install`, copy `.env.example` to `.env`, `npm start`.
Frontend: `cd frontend && npm install && npm run dev`.

Deployment: host `backend/` as a Node web service (set MONGO_URI as an
environment variable) and `frontend/` as a static site (build command
`npm run build`, publish directory `dist`, set VITE_API_URL to the backend URL).
''')],
    output="A full-stack task application in which React sends requests to an Express/Node.js API and the API stores tasks in MongoDB. The project is deployed by hosting its frontend and backend separately.",
    shots=["MERN Task Manager UI", "Cloud deployment dashboard", "GitHub repository (no .env file)"],
    live=False,
    live_note="Deploy the frontend and backend on a cloud host (for example Render, Vercel or Netlify for the frontend). Paste the URLs below after deploying.",
    extra_links=[("Deployed frontend URL", "PASTE_YOUR_FRONTEND_URL_HERE"), ("Deployed backend URL", "PASTE_YOUR_BACKEND_URL_HERE")],
    conclusion="In this experiment I developed a MERN application and followed the process of deploying it. I learned how React, Node.js, Express.js and MongoDB work together, why the API URL and database string must be set through environment variables, and why secret files must stay out of the repository.",
)
