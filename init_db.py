import sqlite3

def initialize_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create users table with username, email, and password
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

if __name__ == '__main__':
    initialize_database()

