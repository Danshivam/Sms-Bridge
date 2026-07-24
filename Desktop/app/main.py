from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="SMS Bridge",
    version="1.0.0"
)


class NotificationMessage(BaseModel):
    app: str
    title: str
    message: str
    timestamp: int


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "SMS Bridge Server Running"
    }


@app.post("/notification")
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