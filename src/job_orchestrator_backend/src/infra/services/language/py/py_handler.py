import subprocess

class PyHandler:

  def _return_message(self, response):
    if response.returncode == 0:
      return { "message": "Success", "status_code": 200 }
    else:
      return { "message": f"Error: {response.stderr}", "status_code": 500 }

  def _dependency_handler(self, dependency: str):
    pass

  def execute(self, path: str, dependency: str = None):
    response = subprocess.run(["python", path], capture_output=True, text=True)   
    return self._return_message(response=response)
    