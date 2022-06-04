from dataclasses import dataclass


@dataclass
class WordModel:
    word: str
    id: int = None
    is_product: bool = None
    idf: float = None
    created_at: str = None
