from dataclasses import dataclass


@dataclass
class ReqWordModel:
    req_id: int
    word_id: int
    id: int = None
    tf: float = None
    tfidf: float = None
