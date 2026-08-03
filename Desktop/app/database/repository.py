from .database import connection, cursor

print("Repository Loaded")

def save_notification(notification):
    print("Saving notification...")