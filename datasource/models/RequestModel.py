from dataclasses import dataclass


@dataclass
class RequestModel:
    id: int
    req: str
    createdBy: int
    createdAt: str
