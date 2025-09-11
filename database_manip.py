import sqlite3

# Connect to or create a SQLite database file
db = sqlite3.connect('student_db.db')

# Get a cursor object to interact with the database
cursor = db.cursor()

# Create the python programming table if it does not exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS python_programming (
    id INTEGER PRIMARY KEY,
    name, TEXT,
    grade INTEGER
)
''')
db.commit()

# Insert multiple records
student_data = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]

# To update existing records with new values, you can use the 'INSERT OR REPLACE' statement
cursor.executemany('''
INSERT OR REPLACE INTO python_programming (id, name, grade)
VALUES (?, ?, ?)
''', student_data)
print('Multiple users inserted or inserted.')

# Checking for Existing IDs
for student in student_data:
    cursor.execute('SELECT * FROM python_programming WHERE id = ?', (student[0],))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO python_programming (id, name, grade) VALUES (?, ?, ?)', student)
    else:
        print(f"Student with ID {student[0]} already exists.")

# Fetch records with grade between 60 and 80
cursor.execute('SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80')
records = cursor.fetchall()
for record in records:
    print(record)

# Update Carl Davis's grade
cursor.execute('UPDATE python_programming SET grade = ? WHERE name = ?', (65, 'Carl Davis'))

# Delete Dennis Fredickson's record
cursor.execute('DELETE  FROM python_programming WHERE name = ?', ('Dennis Fredrickson',))

# Commit the changes
db.commit()

# Change grade of students with id greater than 55 to 80
cursor.execute('UPDATE python_programming SET grade = ? WHERE id > ?', (80, 55))

# Commit the changes and close the database connection
db.commit()
db.close()
print('Database operations completed successfully.')