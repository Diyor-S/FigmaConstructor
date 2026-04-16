from fastapi import FastAPI, APIRouter

from api.v1 import tasks_router

app = FastAPI(
    title="Figma Constructor",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)
app.include_router(tasks_router)
