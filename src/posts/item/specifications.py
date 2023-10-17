from src.specification import Specification
from src.posts.item.models import Item


class ItemByIdSpecification(Specification):
    def is_satisfied(self, candidate):
        return Item.id == candidate


class ItemIsActiveSpecification(Specification):
    def is_satisfied(self, candidate=True):
        return Item.is_active == candidate


class ItemWithImg(Specification):
    def is_satisfied(self, candidate=None):
        return Item.img_url != candidate
