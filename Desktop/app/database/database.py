import sqlite3

Sms_eater = "sms_bridge.db"
connection = sqlite3.connect(Sms_eater)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    app TEXT,
    title TEXT,
    message TEXT,
    timestamp INTEGER
)
""")

print("Database module loaded")
