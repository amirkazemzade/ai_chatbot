from dataclasses import dataclass


@dataclass
class RequestResponseModel:
    id: int = 0
    req_id: int = 0
    resp_id: int = 0
    created_at: str = ''
