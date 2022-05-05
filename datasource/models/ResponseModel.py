from dataclasses import dataclass


@dataclass
class ResponseModel:
    id: int
    req: str
    createdAt: str
