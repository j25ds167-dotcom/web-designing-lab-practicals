function addTask() {
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
