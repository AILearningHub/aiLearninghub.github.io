from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/register.html', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match. Please try again.')
            return redirect(url_for('register_page'))

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        
        conn = get_db_connection()
        conn.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, hashed_password))
        conn.commit()
        conn.close()

        flash('Registration successful! Please log in.')
        return redirect(url_for('login_page'))

    return render_template('register.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()
        
        if user and bcrypt.checkpw(password.encode(), user['password']):
            flash('Login successful!')
            return redirect(url_for('main_page'))
        else:
            flash('Invalid email or password. Please try again.')

    return render_template('login.html')

@app.route('/')
def main_page():
    return 'This is the main page.'

if __name__ == '__main__':
    app.run(debug=True)
