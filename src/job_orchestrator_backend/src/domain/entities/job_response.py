from dataclasses import dataclass


@dataclass
class JobResponseDto:
  message: str
  status_code: int