from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="SMS Bridge",
    version="1.0.0"
)


class TestMessage(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "SMS Bridge Server Running"
    }


@app.post("/message")
def receive_message(message: TestMessage):

    print("\n==============================")
    print("Received from Android")
    print(message.message)
    print("==============================\n")

    return {
        "status": "received"
    }