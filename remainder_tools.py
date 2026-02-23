import sqlite3

DB = "database/reminders.db"

def init_db():

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS reminders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            time TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_reminder(text, time):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO reminders(text,time) VALUES (?,?)",
        (text, time)
    )

    conn.commit()
    conn.close()

    return "Reminder added"


def get_reminders():

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT * FROM reminders")

    rows = cur.fetchall()

    conn.close()

    return rows