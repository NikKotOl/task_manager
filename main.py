from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from database import create_tables, drop_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    print("ВЫКЛЮЧЕНИЕ!!!!!!!!!!")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def greeting():
    return "Welcome to task manager!"

app.include_router(tasks_router)