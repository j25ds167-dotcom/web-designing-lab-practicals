import { useState } from "react";
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
