from abc import ABC, abstractmethod


class LanguageFactoryInterface(ABC):

  @abstractmethod
  def handler(self, language: str):
    pass