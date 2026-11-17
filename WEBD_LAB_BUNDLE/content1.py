NAME = "Aniket Chaudhary"
ROLL = "J250212025"
GH_USER = "j25ds167-dotcom"
EMAIL = "j25ds167@jssuninoida.edu.in"


def live(n):
    return "https://%s.github.io/Webd-exp-%d/" % (GH_USER, n)


def repo(n):
    return "https://github.com/%s/Webd-exp-%d" % (GH_USER, n)


EXP1 = dict(
    n=1,
    title="Set up a GitHub repository, branches, merge changes, and host a static website using GitHub Pages.",
    aim="To practise version control using Git and GitHub by creating a repository, managing branches, merging changes, and publishing a static website.",
    desc="Git is a distributed version-control system used to track changes in source code. GitHub hosts Git repositories and supports collaboration. Branches allow developers to work independently; merging combines completed work. GitHub Pages publishes static HTML, CSS, and JavaScript files as a website.",
    software=["VS Code (code editor)", "Git and GitHub (version control and online repository)", "GitHub Desktop", "HTML and CSS", "GitHub Pages (free hosting)", "Web browser (Google Chrome)"],
    files=[("index.html", r'''<!DOCTYPE html>
<html>
<head>
<title>Web Design Experiment 1</title>
<style>
body { font-family: Arial; background: #f4f4f4; text-align: center; }
header { background: #333; color: white; padding: 15px; }
section { padding: 15px; }
</style>
</head>
<body>
<header>
<h2>Web Design Experiment 1</h2>
<p>GitHub Repository and GitHub Pages</p>
</header>
<section>
<h3>Welcome to My Webpage</h3>
<p>This is my first hosted website.</p>
</section>
<section>
<h3>About</h3>
<p>GitHub is used to store and manage projects.</p>
</section>
<section>
<h3>Contact</h3>
<p>Name: Aniket Chaudhary</p>
<p>Email: j25ds167@jssuninoida.edu.in</p>
</section>
</body>
</html>
''')],
    output="A GitHub repository containing the website source files, a merged feature branch, and a publicly accessible GitHub Pages URL.",
    shots=["Webpage (GitHub Pages)", "GitHub repository", "Branch and merge (git log --graph)"],
    live=True,
    conclusion="In this experiment I created a GitHub repository and uploaded a simple HTML and CSS webpage to it. I created a feature branch, edited the code there, and merged it back into the main branch. I then turned on GitHub Pages to publish the page online. This showed me how version control tracks changes and how Git and GitHub support working in a team.",
)

EXP2 = dict(
    n=2,
    title="Develop a personal portfolio webpage using HTML and CSS.",
    aim="To design a personal portfolio webpage that presents personal information, education details and a declaration using HTML forms, tables and CSS.",
    desc="HTML provides the structure of a webpage, while CSS controls its appearance and layout. This portfolio page uses a form with text inputs, a dropdown, date picker, radio buttons, a table for education details and a checkbox declaration. The CSS is kept in a separate file to keep the code clean.",
    software=["VS Code (code editor)", "Git and GitHub (version control and online repository)", "GitHub Desktop", "HTML and CSS", "GitHub Pages (free hosting)", "Web browser (Google Chrome)"],
    files=[("index.html", r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Portfolio</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<form>
<h1>Portfolio</h1>
<b>Name:</b><input type="text" required>
<b>Father's Name:</b><input type="text">
<b>Mother's Name:</b><input type="text">
<b>Country:</b>
<select><option>Select Country</option><option>India</option><option>USA</option><option>UK</option></select>
<b>Date of Birth:</b><input type="date">
<b>Gender:</b>
<input type="radio" name="g"> Male
<input type="radio" name="g"> Female
<input type="radio" name="g"> Other
<h3>Education Qualification</h3>
<small>Enter your education details in the table below.</small>
<table>
<tr><th>S. No.</th><th>Standard</th><th>Board / University</th><th>Passing Year</th><th>Percentage</th></tr>
<tr><td>1</td><td><input type="text"></td><td><input type="text"></td><td><input type="text"></td><td><input type="text"></td></tr>
<tr><td>2</td><td><input type="text"></td><td><input type="text"></td><td><input type="text"></td><td><input type="text"></td></tr>
<tr><td>3</td><td><input type="text"></td><td><input type="text"></td><td><input type="text"></td><td><input type="text"></td></tr>
</table>
<b>Selected Course:</b>
<input type="radio" name="c"> B.Tech
<input type="radio" name="c"> M.Tech
<h3>Declaration</h3>
<input type="checkbox" required>
I declare that the information given above is correct.
<p class="buttons">
<button type="submit">Submit</button>
<button type="reset">Reset</button>
</p>
</form>
</body>
</html>
'''), ("style.css", r'''body {
  font-family: Arial;
  background: #f1f4fa;
  padding: 15px;
  color: #333;
}
form {
  background: white;
  max-width: 850px;
  margin: auto;
  padding: 25px;
  border: 1px solid #ddd;
  border-radius: 8px;
}
h1 {
  text-align: center;
  color: #294b70;
}
h3 { color: #294b70; }
input[type=text], input[type=date], select {
  width: 100%;
  box-sizing: border-box;
  padding: 9px;
  margin: 7px 0 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}
th, td {
  border: 1px solid #999;
  padding: 7px;
  text-align: center;
}
th { background: #e7edf7; }
td input {
  width: 95%;
  box-sizing: border-box;
  padding: 7px;
  border: 1px solid #ddd;
}
button {
  padding: 10px 25px;
  background: #294b70;
  color: white;
  border: 0;
  border-radius: 4px;
  cursor: pointer;
}
.buttons { text-align: center; }
.buttons button:last-child { background: #687586; }
''')],
    output="A styled personal portfolio form page with personal details fields, an education table, course selection, a declaration checkbox, and Submit and Reset buttons.",
    shots=["Portfolio page", "GitHub repository"],
    live=True,
    conclusion="In this experiment I built a personal portfolio page using HTML and CSS. I used form controls such as text boxes, a dropdown, radio buttons and a table, and I kept the styling in a separate CSS file. I learned how forms, tables and basic CSS properties work together, and I published the page with GitHub Pages.",
)

EXP3 = dict(
    n=3,
    title="Create a dynamic To-Do List application using JavaScript and DOM manipulation.",
    aim="To develop an interactive To-Do List that allows users to add, delete, and mark tasks as completed using JavaScript.",
    desc="The Document Object Model (DOM) represents an HTML page as a tree of objects. JavaScript can select elements, create new elements, change text or classes, and respond to user events. An event listener handles actions such as clicking an Add or Delete button. The application can maintain tasks in an array and optionally store them in localStorage.",
    software=["VS Code (code editor)", "Git and GitHub", "Web browser (Google Chrome)", "GitHub Pages (free hosting)"],
    files=[("index.html", r'''<!DOCTYPE html>
<html>
<head>
  <title>To-Do List</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <h1>My To-Do List</h1>
    <input type="text" id="taskInput" placeholder="Enter a task">
    <button onclick="addTask()">Add Task</button>
    <ul id="taskList"></ul>
  </div>
  <script src="script.js"></script>
</body>
</html>
'''), ("style.css", r'''body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
.container {
  width: 500px;
  padding: 30px;
  background: white;
  border-radius: 10px;
  text-align: center;
}
h1 {
  font-size: 32px;
}
input {
  width: 300px;
  padding: 12px;
  font-size: 16px;
}
button {
  padding: 10px 15px;
  font-size: 16px;
  cursor: pointer;
}
li {
  font-size: 18px;
  padding: 8px;
}
li.completed {
  text-decoration: line-through;
  color: gray;
}
'''), ("script.js", r'''function addTask() {
  var input = document.getElementById("taskInput");
  var task = input.value.trim();

  if (task === "") {
    alert("Please enter a task");
    return;
  }

  var li = document.createElement("li");
  li.textContent = task;

  // Click a task to mark it as completed
  li.onclick = function () {
    li.classList.toggle("completed");
  };

  // Create a delete button
  var deleteButton = document.createElement("button");
  deleteButton.textContent = "Delete";
  deleteButton.onclick = function (event) {
    event.stopPropagation();
    li.remove();
  };

  li.appendChild(deleteButton);
  document.getElementById("taskList").appendChild(li);
  input.value = "";
}
''')],
    output="A To-Do List webpage where a user can add tasks, mark them as completed by clicking them, and delete them.",
    shots=["To-Do List webpage", "GitHub repository"],
    live=True,
    conclusion="In this experiment I created a dynamic To-Do List using HTML, CSS and JavaScript. I learned how to select elements, create new elements, handle click events, and update the page through DOM manipulation without reloading it.",
)

EXP4 = dict(
    n=4,
    title="Optimize a webpage for SEO and accessibility using semantic HTML, heading structure, and meta tags.",
    aim="To improve the search-engine visibility and accessibility of a webpage by applying semantic HTML, meaningful headings, metadata, and accessible attributes.",
    desc="Search Engine Optimization (SEO) helps search engines understand webpage content. Semantic HTML gives meaning to page regions. A logical heading hierarchy helps users and assistive technologies understand content structure. The title and meta description summarize a page in search results. Accessibility practices include descriptive alt text, labels for form controls, keyboard navigation, and sufficient color contrast.",
    software=["VS Code", "Google Chrome (or any modern web browser)"],
    files=[("index.html", r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="A simple webpage about learning web design.">
  <meta name="keywords" content="HTML, CSS, web design, learning">
  <meta name="author" content="Aniket Chaudhary">
  <title>Learning Web Design | Home</title>
</head>
<body>
  <header>
    <h1>Learning Web Design</h1>
    <p>A beginner's guide to creating websites.</p>
  </header>

  <nav aria-label="Main navigation">
    <a href="#about">About</a> |
    <a href="#topics">Topics</a> |
    <a href="#contact">Contact</a>
  </nav>

  <main>
    <section id="about">
      <h2>About This Website</h2>
      <p>This website shares basic information about web design.</p>
      <img src="web-design.jpg" alt="Laptop showing a website design" width="250">
    </section>

    <section id="topics">
      <h2>Topics</h2>
      <article>
        <h3>HTML</h3>
        <p>HTML provides the structure of a webpage.</p>
      </article>
      <article>
        <h3>CSS</h3>
        <p>CSS is used to style a webpage.</p>
      </article>
    </section>

    <section id="contact">
      <h2>Contact Us</h2>
      <form>
        <label for="email">Email address:</label>
        <input type="email" id="email" name="email">
        <button type="submit">Submit</button>
      </form>
    </section>
  </main>

  <footer>
    <p>&copy; 2026 Learning Web Design</p>
  </footer>
</body>
</html>
''')],
    output="A webpage using semantic elements, a logical heading hierarchy, descriptive meta tags, navigation, and accessible form labels and image text.",
    shots=["Webpage output", "GitHub repository"],
    live=True,
    conclusion="In this experiment I optimized a webpage for SEO and accessibility. I used semantic tags such as header, nav, main, section and footer, a proper heading order, meta tags, form labels and alt text for the image. These changes make the page easier for search engines and for users of assistive technology to understand.",
)

EXP5 = dict(
    n=5,
    title="Create a weather application using Fetch API or Axios.",
    aim="To build a weather application that accepts a city name and displays current weather information retrieved from a weather API.",
    desc="A web API allows an application to request data from a remote service. The Fetch API provides a JavaScript interface for making HTTP requests and returns a Promise. The response is commonly converted to JSON. A weather service may return temperature, humidity, wind speed, and weather conditions. This experiment uses the free Open-Meteo APIs, which do not need an API key.",
    software=["VS Code", "A modern web browser with an internet connection"],
    files=[("index.html", r'''<!DOCTYPE html>
<html>
<head>
  <title>Weather App</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="box">
    <h1>Weather App</h1>
    <input type="text" id="city" placeholder="Enter city name">
    <button onclick="getWeather()">Get Weather</button>
    <div id="result">Enter a city to see its weather.</div>
  </div>
  <script src="script.js"></script>
</body>
</html>
'''), ("style.css", r'''body {
  font-family: Arial;
  background: #e8f3ff;
}
.box {
  width: 340px;
  margin: 80px auto;
  padding: 25px;
  background: white;
  text-align: center;
  border-radius: 10px;
}
input, button {
  padding: 10px;
  margin: 5px;
}
#result {
  margin-top: 20px;
  line-height: 1.8;
}
'''), ("script.js", r'''async function getWeather() {
  var city = document.getElementById("city").value.trim();
  var result = document.getElementById("result");

  if (city === "") {
    result.textContent = "Please enter a city name.";
    return;
  }

  result.textContent = "Loading...";

  try {
    // Find the latitude and longitude of the city
    var placeResponse = await fetch(
      "https://geocoding-api.open-meteo.com/v1/search?name="
      + encodeURIComponent(city) + "&count=1"
    );
    var placeData = await placeResponse.json();

    if (!placeData.results) {
      result.textContent = "City not found.";
      return;
    }

    var place = placeData.results[0];

    // Get current weather using the coordinates
    var weatherResponse = await fetch(
      "https://api.open-meteo.com/v1/forecast?latitude="
      + place.latitude + "&longitude=" + place.longitude
      + "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    );
    var weatherData = await weatherResponse.json();
    var current = weatherData.current;

    result.innerHTML =
      "<h3></h3>" +
      "Temperature: " + current.temperature_2m + " &deg;C<br>" +
      "Humidity: " + current.relative_humidity_2m + " %<br>" +
      "Wind Speed: " + current.wind_speed_10m + " km/h";
    // Set the city name as text (safer than building it into HTML)
    result.querySelector("h3").textContent = place.name;
  } catch (error) {
    result.textContent = "Unable to get weather. Check your internet.";
  }
}
''')],
    output="The application displays the selected city's current temperature, humidity, and wind speed.",
    shots=["Weather app showing a city's weather", "GitHub repository"],
    live=True,
    conclusion="In this experiment I created a weather application with the JavaScript Fetch API. I learned how to send requests to an API, wait for the response with async and await, read JSON data, handle errors, and show the result on a webpage.",
)

EXP6 = dict(
    n=6,
    title="Build a responsive blog website using media queries and Bootstrap.",
    aim="To create a responsive blog website that adapts its layout to mobile, tablet, and desktop screen sizes using CSS media queries and Bootstrap.",
    desc="Responsive web design ensures that content remains usable on different screen sizes. CSS media queries apply styles according to viewport conditions. Bootstrap provides a responsive grid system and reusable components such as navigation bars, cards, and buttons. A mobile-first layout starts with small screens and progressively enhances the design for larger screens.",
    software=["VS Code", "Google Chrome (internet connection required for the Bootstrap CDN)"],
    files=[("index.html", r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>My Blog</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <nav class="navbar navbar-dark bg-dark">
    <div class="container">
      <a class="navbar-brand" href="#">My Blog</a>
    </div>
  </nav>

  <header class="text-center p-5 bg-light">
    <h1>Welcome to My Blog</h1>
    <p>Articles about technology and learning.</p>
  </header>

  <main class="container my-4">
    <div class="row">
      <div class="col-md-4 mb-3">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title">Learning HTML</h3>
            <p class="card-text">HTML gives structure to webpages.</p>
            <a href="#" class="btn btn-primary">Read More</a>
          </div>
        </div>
      </div>
      <div class="col-md-4 mb-3">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title">Learning CSS</h3>
            <p class="card-text">CSS makes webpages attractive.</p>
            <a href="#" class="btn btn-primary">Read More</a>
          </div>
        </div>
      </div>
      <div class="col-md-4 mb-3">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title">Learning JavaScript</h3>
            <p class="card-text">JavaScript adds interactivity.</p>
            <a href="#" class="btn btn-primary">Read More</a>
          </div>
        </div>
      </div>
    </div>
  </main>

  <footer class="text-center bg-dark text-white p-3">
    &copy; 2026 My Blog. All rights reserved. - By Aniket Chaudhary
  </footer>
</body>
</html>
'''), ("style.css", r'''body {
  font-family: Arial;
}
.card {
  height: 100%;
}
.card:hover {
  box-shadow: 0 3px 10px #999;
}

/* Styles for small screens */
@media (max-width: 600px) {
  header {
    padding: 25px !important;
  }
  header h1 {
    font-size: 25px;
  }
}
''')],
    output="A responsive blog webpage with a navigation bar, three article cards, and a footer. The layout adjusts for smaller screens.",
    shots=["Blog on desktop width", "Blog on mobile width (Chrome DevTools)", "GitHub repository"],
    live=True,
    conclusion="In this experiment I created a responsive blog website with Bootstrap and CSS media queries. I learned how the Bootstrap grid classes and media queries let a page rearrange itself for desktop, tablet and mobile screens.",
)
