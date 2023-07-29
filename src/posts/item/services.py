from typing import Iterator

from src.services import BaseServices

from src.posts.item.repositories import ItemRepository
from src.posts.item.schemas import Item
from src.posts.item.specifications import ItemByIdSpecification, ItemIsActiveSpecification, ItemIsInactiveSpecification


class ItemService(BaseServices):
    def __init__(self, item_repository: ItemRepository):
        super().__init__(repository=item_repository)

    def get_item_by_id(self, item_id: int) -> Item:
        spec = ItemByIdSpecification().is_satisfied(item_id)
        return self._repository.get(spec)

    def get_items(self) -> Iterator[Item]:
        return self._repository.list()

    def get_active_items(self) -> Iterator[Item]:
        spec = ItemIsActiveSpecification().is_satisfied()
        return self._repository.list(spec=spec)

    def get_inactive_items(self) -> Iterator[Item]:
        spec = not ItemIsActiveSpecification().is_satisfied()
        return self._repository.list(spec)
