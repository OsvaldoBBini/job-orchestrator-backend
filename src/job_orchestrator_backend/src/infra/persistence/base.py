from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from job_orchestrator_backend.src.infra.persistence.models import Base

class Ticket(Base):
  __tablename__ = "tickets"
  id: Mapped[str] = mapped_column(String, primary_key=True)
  name: Mapped[str] = mapped_column(String)
  owner: Mapped[str] = mapped_column(String)

class Log(Base):
  __tablename__ = "logs"
  id: Mapped[str] = mapped_column(String, primary_key=True)
  log_id: Mapped[str] = mapped_column(String)
  status: Mapped[str] = mapped_column(String)
  description: Mapped[str] = mapped_column(String)
  

  
