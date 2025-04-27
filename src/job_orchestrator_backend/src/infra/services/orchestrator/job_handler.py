import os
from job_orchestrator_backend.src.domain.entities.job_response import JobResponseDto
from job_orchestrator_backend.src.domain.factories.language_factory import LanguageFactoryInterface
from job_orchestrator_backend.src.domain.services.JobHandler.job_handler import JobHandlerInterface

class JobHandler(JobHandlerInterface):

  def __init__(self, factory: LanguageFactoryInterface):
    self._factory = factory
    self._root_path = os.path.join(os.getcwd().split("src")[0], "src")
    self._dir_folder = os.path.join(self._root_path, "codes")
  
  def _check_code_file_type(self, file_name):
    return file_name.split('.')[-1]
  
  def _get_files(self, id: str):
    folder_path = os.path.join(self._dir_folder, id)
    files = os.listdir(folder_path)
    code_file = list(filter(lambda file: 'code' in file, files))[0]
    dependencies = list(filter(lambda file: 'code' not in file, files)) 
    dependency_file = None if len(dependencies) == 0 else os.path.join(folder_path, dependencies[0])
    return os.path.join(folder_path, code_file) , dependency_file
  
  async def execute_job(self, id: str) -> JobResponseDto:
    code, dependency = self._get_files(id)
    file_type = self._check_code_file_type(file_name=code)
    language_handler = self._factory.handler(language=file_type) 
    response = await language_handler(path=code, dependency=dependency)
    return response