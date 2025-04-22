from job_orchestrator_backend.src.infra.services.language.py.py_handler import PyHandler


class LanguageFactory:

  def handler(self, language: str):

    available_langague = {
      "py": PyHandler()
    }

    return available_langague[language].execute