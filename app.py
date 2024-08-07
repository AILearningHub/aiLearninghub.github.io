from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match. Please try again.')
            return redirect(url_for('register_page'))

        # Add your user registration logic here (e.g., save to database)

        flash('Registration successful! Please log in.')
        return redirect(url_for('login_page'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Add your login logic here (e.g., check credentials)

        return redirect(url_for('main_page'))

    return render_template('login.html')

@app.route('/')
def main_page():
    return 'This is the main page.'

if __name__ == '__main__':
    app.run(debug=True)
