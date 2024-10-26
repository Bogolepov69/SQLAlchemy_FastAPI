from fastapi import FastAPI, APIRouter
from app.routers import task
from app.routers import user

app = FastAPI()
api_router = APIRouter()


@app.get("/")
async def welcome() -> dict:
    return {"message": "My taskmanager project"}


app.include_router(user.router)
app.include_router(task.router)

