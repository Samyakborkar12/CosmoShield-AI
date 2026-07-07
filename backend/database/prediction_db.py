import sqlite3


def save_prediction(satellite, energy, radiation, risk):

    conn = sqlite3.connect("cosmoshield.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predictions
        (satellite, energy, radiation, risk)
        VALUES (?, ?, ?, ?)
    """, (satellite, energy, radiation, risk))

    conn.commit()
    conn.close()