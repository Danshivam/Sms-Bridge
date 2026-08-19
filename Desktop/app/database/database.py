import sqlite3

Sms_eater = "sms_bridge.db"

def get_connection():

    connection = sqlite3.connect(Sms_eater)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    return connection, cursor


# cursor.execute("""
# CREATE TABLE IF NOT EXISTS notifications (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     app TEXT,
#     title TEXT,
#     message TEXT,
#     timestamp INTEGER
# )
# """)

# print("Database module loaded")

