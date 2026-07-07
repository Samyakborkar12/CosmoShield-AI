from backend.database.db import get_connection


def save_prediction(satellite, energy, radiation, risk):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predictions
        (satellite, energy, radiation, risk)
        VALUES (?, ?, ?, ?)
    """, (satellite, energy, radiation, risk))

    conn.commit()
    conn.close()