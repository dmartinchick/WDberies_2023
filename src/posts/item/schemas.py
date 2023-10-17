from pydantic import BaseModel, Field


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
