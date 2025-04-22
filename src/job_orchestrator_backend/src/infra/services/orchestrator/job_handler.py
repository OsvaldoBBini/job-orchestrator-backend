import os

class JobHandler:

  def __init__(self, factory):
    self._factory = factory
    self._dir_folder = os.path.join(os.getcwd(), "src\\codes")
  
  def _check_code_file_type(self, file_name):
    return file_name.split('.')[-1]
  
  def _get_files(self, id: str):
    folder_path = os.path.join(self._dir_folder, id)
    files = os.listdir(folder_path)
    code_file = list(filter(lambda file: 'code' in file, files))[0]
    dependency_file = list(filter(lambda file: 'code' not in file, files))[0]
    return os.path.join(folder_path, code_file) , os.path.join(folder_path, dependency_file)
  
  def execute_job(self, id: str):
    code, dependency = self._get_files(id)
    file_type = self._check_code_file_type(file_name=code)
    language_handler = self._factory.handler(language=file_type) 
    response = language_handler(path=code, dependency=dependency)
    return response