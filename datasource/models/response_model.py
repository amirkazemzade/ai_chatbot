from dataclasses import dataclass


@dataclass
class ResponseModel:
    id: int
    resp: str
    createdAt: str
