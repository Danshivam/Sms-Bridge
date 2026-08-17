from .database import get_connection
from ..models import NotificationMessage
from ..utils import format_timestamp
from ..analyzer import extract_otp

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

    connection, cursor = get_connection()

    try:
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
                timestamp=row[4],
                formatted_time = format_timestamp(row[4])   
            )
            
            otp = extract_otp(notification.message)

            if otp:
                notification.otp = otp
                notification.is_otp = True

            notifications.append(notification)
            
        return notifications
         

    finally:

        connection.close()