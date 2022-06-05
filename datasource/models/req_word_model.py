from dataclasses import dataclass


@dataclass
class ReqWordModel:
    id: int = 0
    req_id: int = None
    word_id: int = None
    tf: float = 0
    tfidf: float = None
