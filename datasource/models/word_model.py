from dataclasses import dataclass


@dataclass
class WordModel:
    id: int = None
    word: str = ''
    idf: float = None
    is_product: bool = None
    created_at: str = None
