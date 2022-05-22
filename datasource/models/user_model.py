from dataclasses import dataclass


@dataclass
class UserModel:
    id: int
    telId: int
    createdAt: str
