from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from .routes import router
from fastapi.staticfiles import StaticFiles
import json
from app.database.repository import get_notifications


app = FastAPI(
    title="SMS Bridge",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(router)


@app.get("/")
def home(request: Request):

    notifications = get_notifications()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "notifications_json": json.dumps(
                [notification.model_dump() for notification in notifications]
            )
        }
    )