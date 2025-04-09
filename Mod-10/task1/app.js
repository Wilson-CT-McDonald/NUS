// task1.js
const express = require('express');
const session = require('express-session');
const db = require('./db');

const app = express();
const PORT = 3000;

app.set('view engine', 'pug');
app.set('views', './views');

app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

app.use(session({
  secret: 'mySecret',
  resave: false,
  saveUninitialized: true
}));

// Routes
app.get('/', (req, res) => {
  db.all('SELECT * FROM items', [], (err, rows) => {
    res.render('index', { items: rows });
  });
});

// Set session
app.get('/login', (req, res) => {
  req.session.username = 'Wilson';
  res.send('Logged in as Wilson');
});

// Check session
app.get('/whoami', (req, res) => {
  const username = req.session.username || 'Guest';
  res.send(`Hello, ${username}`);
});

// Add new item - POST
app.post('/add', (req, res) => {
  const { name } = req.body;
  db.run('INSERT INTO items(name) VALUES (?)', [name], () => {
    res.redirect('/');
  });
});

// CRUD setup
app.get('/edit/:id', (req, res) => {
  db.get('SELECT * FROM items WHERE id = ?', req.params.id, (err, row) => {
    res.render('edit', { item: row });
  });
});

// Edit item - POST (update data)
app.post('/edit/:id', (req, res) => {
  db.run('UPDATE items SET name = ? WHERE id = ?', [req.body.name, req.params.id], () => {
    res.redirect('/');
  });
});

// Delete item
app.get('/delete/:id', (req, res) => {
  db.run('DELETE FROM items WHERE id = ?', req.params.id, () => {
    res.redirect('/');
  });
});

// Initialize the database
db.serialize(() => {
  db.run('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)');
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
