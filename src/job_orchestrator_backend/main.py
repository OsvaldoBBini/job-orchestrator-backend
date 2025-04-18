from fastapi import Depends, FastAPI
from fastapi.concurrency import asynccontextmanager

from job_orchestrator_backend.src.infra.persistence.database import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    database.start_tables()
    yield

app = FastAPI()

@app.get("/")
def read_root(db_session = Depends(database.get_db())):
    print(db_session)
    return {"Hello": "World"}