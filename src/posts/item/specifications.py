from src.specification import Specification
from src.posts.item.schemas import Item


class ItemByIdSpecification(Specification):
    def is_satisfied(self, candidate):
        return Item.id == candidate


class ItemIsActiveSpecification(Specification):
    def is_satisfied(self, candidate=True):
        return Item.is_active == candidate


class ItemIsInactiveSpecification(Specification):
    def is_satisfied(self, candidate=False):
        return Item.is_active == candidate
