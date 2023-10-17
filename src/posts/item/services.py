from typing import Iterator

from loguru import logger
from fastapi import Depends

from src.posts.item.repositories import ItemRepository
from src.posts.item.models import Item
from src.posts.item.specifications import ItemByIdSpecification, ItemIsActiveSpecification
from src.posts.item.specifications import ItemWithImg


class ItemServices:
    def __init__(self, item_repository: ItemRepository = Depends(ItemRepository)):
        self._repository = item_repository

    def get_item_by_id(self, item_id: int) -> Item:
        # TODO: Обработать исключения если item не найден
        spec = ItemByIdSpecification().is_satisfied(item_id)
        return self._repository.get(spec)

    def get_items(self) -> list[Item]:
        return self._repository.list()

    def get_active_items(self) -> list[Item]:
        spec = ItemIsActiveSpecification().is_satisfied()
        return self._repository.list(spec=spec)

    def get_inactive_items(self) -> list[Item]:
        # TODO: не работает.
        spec = ~ItemIsActiveSpecification().is_satisfied()
        return self._repository.list(spec=spec)

    def get_items_with_img(self) -> list[Item]:
        spec = ItemWithImg().is_satisfied()
        return self._repository.list(spec)

    def add_item(self,
                 item_id: int,
                 brand: str,
                 img_url: str,
                 name: str,
                 price: float) -> Item:
        item = Item(id=item_id, brand=brand, img_url=img_url, name=name, price=price)
        return self._repository.add(item)

    def update_item_point(self, item_id: int, new_point: float) -> Item:
        item = self.get_item_by_id(item_id)
        item.point = new_point
        return self._repository.update(item)

    def update_activate_item(self, item_id: int) -> Item:
        item = self.get_item_by_id(item_id)
        item.is_active = True
        return self._repository.update(item)

    def update_deactivate_item(self, item_id: int) -> Item:
        item = self.get_item_by_id(item_id)
        item.is_active = False
        return self._repository.update(item)
