import sqlite3
from config import Config

def get_db_connection():
    """Creates and returns a database connection."""
    conn = sqlite3.connect(Config.DB_PATH)
    return conn

def init_db():
    """Initializes the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transcripts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            text TEXT
        )
    """)
    conn.commit()
    conn.close()
