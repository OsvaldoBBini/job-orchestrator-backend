
from fastapi import FastAPI
from job_orchestrator_backend.src.infra.persistence.database import database
from job_orchestrator_backend.src.infra.services.orchestrator.job_handler import JobHandler
from job_orchestrator_backend.src.infra.factories.language_factory import LanguageFactory

app = FastAPI()
database.start_tables()

@app.get("/")
async def read_root():
    response = await JobHandler(factory=LanguageFactory()).execute_job("1")
    return response