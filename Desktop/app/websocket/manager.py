from fastapi import WebSocket
import json


class ConnectionManager:

    def __init__(self):
        self.connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.connections:
            self.connections.remove(websocket)

    async def send_text(self, message: str):
        for connection in self.connections:
            await connection.send_text(message)

    async def send_notification(self, notification):

        data = {
            "app": notification.app,
            "title": notification.title,
            "message": notification.message,
            "timestamp": notification.timestamp,
            "formatted_time": notification.formatted_time,

            "otp": notification.otp,
            "is_otp": notification.is_otp
                }

        message = json.dumps(data)

        for connection in self.connections:
            await connection.send_text(message)

manager = ConnectionManager()