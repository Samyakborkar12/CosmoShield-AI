from backend.database.db import get_connection


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS satellites(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            satellite TEXT NOT NULL,
            radiation REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()