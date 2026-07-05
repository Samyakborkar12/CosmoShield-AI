from database.db import get_connnection

def create_tables():
    conn = get_connnection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   satellite TEXT,
                   radiation REAL,
                   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP     
        )
    """)

    conn.commit()
    conn.close()
    