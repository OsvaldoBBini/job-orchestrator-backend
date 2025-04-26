from abc import ABC, abstractmethod

from job_orchestrator_backend.src.domain.entities.job_response import JobResponseDto


class JobHandlerInterface(ABC):

  @abstractmethod
  def execute_job(self, id: str) -> JobResponseDto:
    pass