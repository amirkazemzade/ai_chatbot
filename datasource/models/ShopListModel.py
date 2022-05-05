from dataclasses import dataclass


@dataclass
class ShopListModel:
    id: int
    user_id: int
    createdAt: str
