from dataclasses import dataclass


@dataclass
class RequestResponseModel:
    id: int
    req_id: int
    resp_id: int
    created_at: str
