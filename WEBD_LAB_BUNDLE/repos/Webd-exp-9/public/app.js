const registerForm = document.getElementById("registerForm");
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
