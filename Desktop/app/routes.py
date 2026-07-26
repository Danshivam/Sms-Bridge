from fastapi import APIRouter
from .models import NotificationMessage
from .storage import notifications
from fastapi import WebSocket, WebSocketDisconnect
from .websocket.manager import manager

router = APIRouter()

@router.post("/notification")
def receive_notification(notification: NotificationMessage):

    notifications.append(notification)

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

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)
    await manager.send_text("Hello Browser 👋")

    print("🟩 Browser Connected")

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:

        manager.disconnect(websocket)

        print("🟥 Browser Disconnected")