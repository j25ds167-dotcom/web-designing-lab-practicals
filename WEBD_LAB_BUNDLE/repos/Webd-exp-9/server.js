require("dotenv").config();

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
