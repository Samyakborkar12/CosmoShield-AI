import sqlite3


def create_prediction_table():
    conn = sqlite3.connect("cosmoshield.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        satellite TEXT NOT NULL,
        energy REAL NOT NULL,
        radiation REAL NOT NULL,
        risk TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()