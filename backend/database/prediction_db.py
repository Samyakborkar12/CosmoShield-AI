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


def get_recent_predictions(limit=10):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            satellite,
            radiation,
            risk,
            created_at
        FROM predictions
        ORDER BY created_at DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    predictions = []

    for row in rows:

        predictions.append({
            "satellite": row[0],
            "radiation": row[1],
            "risk": row[2],
            "time": row[3]
        })

    return predictions