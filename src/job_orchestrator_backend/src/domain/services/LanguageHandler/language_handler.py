from abc import ABC, abstractmethod

from job_orchestrator_backend.src.domain.entities.job_response import JobResponseDto


class LanguageHandlerInterface(ABC):

  @abstractmethod
  def execute(self, path: str, dependency: str = None) -> JobResponseDto:
    pass