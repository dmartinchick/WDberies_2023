from pydantic import BaseModel, Field


class Item(BaseModel):

    id: int
    brand: str | None
    img_url: str | None
    is_active: bool = Field(default=True)
    name: str | None
    point: float = Field(default=300.0)
    price: float
