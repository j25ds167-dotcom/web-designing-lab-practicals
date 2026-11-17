const express = require("express");
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
