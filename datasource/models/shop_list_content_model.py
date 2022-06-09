from dataclasses import dataclass


@dataclass
class ShopListContentModel:
    id: int
    listId: int
    productId: int
    quantity: str
    createdBy: str
