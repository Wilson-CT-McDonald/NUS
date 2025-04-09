# py -m pip
# py -m pip install flask

from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'mysecret'

# Database connection
def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create table if not exists
with get_db_connection() as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT NOT NULL)')
    conn.commit()

# Routes
@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return render_template('index.html', items=items)

# Q3 for static assets and session management
@app.route('/login')
def login():
    session['username'] = 'Wilson'
    return 'Logged in as Wilson'

@app.route('/whoami')
def whoami():
    return session.get('username', 'Guest')

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    conn = get_db_connection()
    conn.execute('INSERT INTO items (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return redirect('/')

# Q4, CRUD setup with SQLite
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    if request.method == 'POST':
        new_name = request.form['name']
        conn.execute('UPDATE items SET name = ? WHERE id = ?', (new_name, id))
        conn.commit()
        conn.close()
        return redirect('/')
    item = conn.execute('SELECT * FROM items WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('edit.html', item=item)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM items WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
