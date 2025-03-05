import sqlite3

def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')


    cursor.executemany('''
        INSERT INTO users (name, age) VALUES (?, ?)
    ''', [
        ("Alice", 25),
        ("Bob", 30),
        ("Charlie", 22)
    ])

    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

if __name__ == "__main__":
    create_database()
