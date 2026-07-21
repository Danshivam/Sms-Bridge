from fastapi import FastAPI

app = FastAPI(
    title="SMS Bridge",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "SMS Bridge Server Running"
    }