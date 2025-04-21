import os
from fastapi import Depends, FastAPI
from fastapi.concurrency import asynccontextmanager
from dotenv import load_dotenv

load_dotenv()

from job_orchestrator_backend.src.infra.persistence.database import database

@asynccontextmanager
async def lifespan(app: FastAPI):
    database.start_tables()
    yield

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}