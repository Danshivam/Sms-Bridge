from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="SMS Bridge",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "SMS Bridge Server Running"
    }
