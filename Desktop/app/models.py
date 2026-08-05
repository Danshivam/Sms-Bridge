from pydantic import BaseModel

class NotificationMessage(BaseModel):
    app: str
    title: str
    message: str
    timestamp: int
    formatted_time: str | None = None

    otp: str | None = None
    is_otp: bool = False