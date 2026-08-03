import sqlite3

Sms_eater = "sms_bridge.db"
connection = sqlite3.connect(Sms_eater)
cursor = connection.cursor()

print("Database module loaded")
