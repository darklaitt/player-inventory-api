from pydantic import BaseModel
from typing import List, Optional

class ItemBase(BaseModel):
    name: str
    type: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    class Config:
        orm_mode = True

class PlayerBase(BaseModel):
    username: str

class PlayerCreate(PlayerBase):
    pass

class Player(PlayerBase):
    id: int
    gold: int
    resources: dict = {}
    items: List[Item] = []
    class Config:
        orm_mode = True
