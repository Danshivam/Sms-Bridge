from fastapi import APIRouter
from .models import NotificationMessage
from fastapi import WebSocket, WebSocketDisconnect
from .websocket.manager import manager
from .utils import format_timestamp, get_date_group
from .analyzer import extract_otp
from .database.repository import save_notification

router = APIRouter()

@router.post("/notification")
async def receive_notification(notification: NotificationMessage):

    notification.formatted_time = format_timestamp(notification.timestamp)

    notification.date_group = get_date_group(notification.timestamp)

    otp = extract_otp(notification.message)

    if otp:
        notification.otp = otp
        notification.is_otp = True

    save_notification(notification)                    #saves notification then send to server


    await manager.send_notification(notification)

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
    # await manager.send_text("Hello Browser 👋")

    print("🟩 Browser Connected")

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:

        manager.disconnect(websocket)

        print("🟥 Browser Disconnected")