from pydantic import BaseModel

class NotificationMessage(BaseModel):
    app: str
    title: str
    message: str
    timestamp: int