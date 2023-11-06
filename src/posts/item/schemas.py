from pydantic import BaseModel, Field
from enum import Enum


class Item(BaseModel):

    id: int
    brand: str | None
    img_url: str | None
    is_active: bool = Field(default=True)
    name: str | None
    point: float = Field(default=400.0)
    price: float | None

    class Config:
        orm_mode = True


class Enemy(BaseModel):
    enemy_id: int


class Result(str, Enum):
    ITEM_A_WIN = "item_a"
    DRAW = "draw"
    ITEM_B_WIN = "item_b"


class BattleInfo(BaseModel):
    current_id: int
    enemy_id: int
    result: Result


class FightResult(BaseModel):
    item_a: Item
    item_b: Item
