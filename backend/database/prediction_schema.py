from backend.database.db import get_connection


def create_prediction_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            satellite TEXT NOT NULL,

            energy REAL NOT NULL,

            radiation REAL NOT NULL,

            risk TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()