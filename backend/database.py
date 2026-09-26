import sqlite3


def create_database():
    conn = sqlite3.connect("securepass.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()