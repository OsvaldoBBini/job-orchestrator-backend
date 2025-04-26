import subprocess

from job_orchestrator_backend.src.domain.entities.job_response import JobResponseDto
from job_orchestrator_backend.src.domain.services.LanguageHandler.language_handler import LanguageHandlerInterface

class PyHandler(LanguageHandlerInterface):

  def _return_message(self, response) -> JobResponseDto:
    if response.returncode == 0:
      return JobResponseDto(message="Success", status_code=200)
    else:
      return JobResponseDto(message=f"Error: {response.stderr}", status_code=500)

  def _dependency_handler(self, dependency: str):
    pass

  def execute(self, path: str, dependency: str = None) -> JobResponseDto:
    response = subprocess.run(["python", path], capture_output=True, text=True)   
    return self._return_message(response=response)
    