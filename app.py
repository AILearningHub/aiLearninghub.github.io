from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import bcrypt
import os

app = Flask(__name__, template_folder='.')

app.secret_key = 'your_secret_key'

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    if not os.path.exists('users.db'):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()

initialize_database()

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match. Please try again.')
            return redirect(url_for('register_page'))

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            # Check if username already exists
            cursor.execute('SELECT 1 FROM users WHERE username = ?', (username,))
            if cursor.fetchone():
                flash('Username already exists. Please choose another one.')
                return redirect(url_for('register_page'))
            
            # Check if email already exists
            cursor.execute('SELECT 1 FROM users WHERE email = ?', (email,))
            if cursor.fetchone():
                flash('Email already exists. Please choose another one.')
                return redirect(url_for('register_page'))
            
            # If both checks pass, insert the new user
            conn.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, hashed_password))
            conn.commit()
            flash('Registration successful! Please log in.')
            return redirect('https://ailearninghub.github.io/login.html')
        except sqlite3.Error as e:
            flash('An error occurred during registration. Please try again.')
            print(f"Database error: {e}")
        finally:
            conn.close()

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        
        if user and bcrypt.checkpw(password.encode(), user['password']):
            flash('Login successful!')
            return redirect('https://ailearninghub.github.io')
        else:
             flash('Username or password is not correct. Please try again.', 'error')

    return render_template('login.html')

@app.route('/')
def home():
    return '''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Home Page</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                button { padding: 10px 20px; font-size: 16px; margin: 10px; }
            </style>
        </head>
        <body>
            <h1>Welcome to the Home Page. Please login or register.</h1>
            <a href="/register"><button>Register</button></a>
            <a href="/login"><button>Login</button></a>
        </body>
        </html>
    '''

@app.route('/index')
def index_page():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
