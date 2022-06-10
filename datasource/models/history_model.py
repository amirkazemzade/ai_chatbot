from dataclasses import dataclass


@dataclass
class HistoryModel:
    id: int = 0
    user_id: int = 0
    last_response: str = ""
    last_product_id: int = 0