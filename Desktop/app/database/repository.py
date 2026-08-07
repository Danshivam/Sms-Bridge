from .database import get_connection
from ..models import NotificationMessage

print("Repository Loaded")

def save_notification(notification):

    connection, cursor = get_connection()

    try:
        cursor.execute("""
            INSERT INTO notifications (
                app,
                title,
                message,
                timestamp
            )
            VALUES (?, ?, ?, ?)
            """, (
            notification.app,
            notification.title,
            notification.message,
            notification.timestamp
            )
        )

        connection.commit()    # Save these changes permanently.

    finally:
        connection.close()

def get_notifications():
    
    cursor.execute("""
        SELECT *
        FROM notifications
        ORDER BY timestamp DESC
        """)

    rows = cursor.fetchall()

    notifications = []

    for row in rows:

        notification = NotificationMessage(
            app=row[1],
            title=row[2],
            message=row[3],
            timestamp=row[4]
        )

        notifications.append(notification)

    return notifications 
