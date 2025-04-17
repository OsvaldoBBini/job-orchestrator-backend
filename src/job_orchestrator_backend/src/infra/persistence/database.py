import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from job_orchestrator_backend.src.infra.persistence.models import Base

load_dotenv()

class DataBase:

  def __init__(self):
    self._connection_url = os.getenv("DB_URL")
    self._engine = create_engine(self._connection_url, echo=True)
  
  def start_tables(self):
    Base.metadata.create_all(bind=self._engine, checkfirst=True)

  def create_session(self) -> Session:
    return Session(self._engine)

session = DataBase().create_session()