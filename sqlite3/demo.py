import sqlite3

# Connect to a local SQLite database (it will create a file if it doesn't exist)
conn = sqlite3.connect('favorites.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Step 1: Create a table (if it doesn't exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Step 2: Insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
conn.commit()  # Commit the transaction to save the changes

# Step 3: Query the data (simple SELECT query)
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Display the query results
for row in rows:
    print(row)  # Each row is a tuple (id, name, age)

# Step 4: Close the connection
conn.close()
