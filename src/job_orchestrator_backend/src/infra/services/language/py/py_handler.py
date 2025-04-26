import shutil
import subprocess
import os
import uuid
from job_orchestrator_backend.src.domain.entities.job_response import JobResponseDto
from job_orchestrator_backend.src.domain.services.LanguageHandler.language_handler import LanguageHandlerInterface

class PyHandler(LanguageHandlerInterface):

  def __init__(self):
    self._os_is_windows = os.name == "nt"
    self._temp_id = uuid.uuid4()
    self._temp_path = os.path.join(os.getcwd(), f"temp{self._temp_id}")
    self._venv_path = os.path.join(os.getcwd(), f"temp{self._temp_id}", "venv")

  def _return_message(self, response) -> JobResponseDto:
    if response.returncode == 1:
      return JobResponseDto(message=f"Error: {response.stderr}", status_code=500)
    return JobResponseDto(message="Success", status_code=200)
  
  def _dependency_installer(self):
    if self._os_is_windows:
      return os.path.join(self._venv_path, "Scripts", "pip.exe")
    return os.path.join(self._venv_path, "bin", "pip")
  
  def _python_executer(self):
    if self._os_is_windows:
        return os.path.join(self._venv_path, "Scripts", "python.exe")
    return os.path.join(self._venv_path, "bin", "python")

  def _dependency_handler(self, dependency: str):
    os.makedirs(self._temp_path, exist_ok=True)
    subprocess.run(["python", "-m", "venv", f"temp{self._temp_id}/venv"], check=True)
    pip_path = self._dependency_installer()
    subprocess.run([pip_path, "install", "-r", dependency], capture_output=True, text=True)

  def execute(self, path: str, dependency: str = None) -> JobResponseDto:
    if dependency:
      self._dependency_handler(dependency)
      python_path = self._python_executer()
      response = subprocess.run([python_path, path], capture_output=True, text=True)
      if os.path.exists(self._temp_path):
        shutil.rmtree(self._temp_path)
    else:
      response = subprocess.run(["python", path], capture_output=True, text=True)   
    return self._return_message(response=response)
