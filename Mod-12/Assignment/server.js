const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

let students = [];
let nextId = 1;

// Validation function
function validateStudent(data) {
  const { name, email, program } = data;
  if (!name || typeof name !== 'string') return false;
  if (!email || typeof email !== 'string') return false;
  if (!program || typeof program !== 'string') return false;
  return true;
}

// GET all students
app.get('/students', (req, res) => {
  res.status(200).json(students);
});

// GET student by ID
app.get('/students/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const student = students.find(s => s.id === id);
  if (!student) {
    return res.status(404).json({ error: 'Student not found' });
  }
  res.status(200).json(student);
});

// POST a new student
app.post('/students', (req, res) => {
  if (!validateStudent(req.body)) {
    return res.status(400).json({ error: 'Invalid student data' });
  }
  const newStudent = { id: nextId++, ...req.body };
  students.push(newStudent);
  res.status(201).json(newStudent);
});

// PUT update student
app.put('/students/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = students.findIndex(s => s.id === id);
  if (index === -1) {
    return res.status(404).json({ error: 'Student not found' });
  }
  if (!validateStudent(req.body)) {
    return res.status(400).json({ error: 'Invalid student data' });
  }
  students[index] = { id, ...req.body };
  res.status(200).json(students[index]);
});

// DELETE student
app.delete('/students/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = students.findIndex(s => s.id === id);
  if (index === -1) {
    return res.status(404).json({ error: 'Student not found' });
  }
  students.splice(index, 1);
  res.status(200).json({ message: 'Student deleted successfully' });
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
