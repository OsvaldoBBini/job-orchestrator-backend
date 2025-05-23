from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from job_orchestrator_backend.src.infra.commun.settings import connection_url
from job_orchestrator_backend.src.infra.persistence.models import Base

class DataBase:
  def __init__(self):
    self._connection_url = connection_url
    self._engine = create_engine(self._connection_url, echo=True, future=True)
    self._SessionLocal = sessionmaker(bind=self._engine, autoflush=False, autocommit=False)

  def start_tables(self):
      Base.metadata.create_all(bind=self._engine, checkfirst=True)

  @contextmanager
  def session_scope(self):
      session = self._SessionLocal()
      try:
          yield session
          session.commit()
      except Exception:
          session.rollback()
          raise
      finally:
          session.close()

  def get_db(self):
      db = self._SessionLocal()
      try:
          yield db
      finally:
          db.close()

database = DataBase()