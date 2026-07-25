from fastapi import APIRouter
from .models import NotificationMessage

router = APIRouter()

@router.post("/notification")
def receive_notification(notification: NotificationMessage):

    print("\n==============================")
    print("Notification Received")
    print("==============================")
    print(f"App      : {notification.app}")
    print(f"Title    : {notification.title}")
    print(f"Message  : {notification.message}")
    print(f"Time     : {notification.timestamp}")
    print("==============================\n")

    return {
        "status": "received"
    }