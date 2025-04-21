from fastapi import FastAPI
from job_orchestrator_backend.src.infra.persistence.database import database

app = FastAPI()
database.start_tables()

@app.get("/")
def read_root():
    return {"Hello": "World"}