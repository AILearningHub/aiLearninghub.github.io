import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Execute a query
cursor.execute('SELECT * FROM users')

# Fetch all results
rows = cursor.fetchall()

# Print results
for row in rows:
    print(row)

# Close the connection
conn.close()
