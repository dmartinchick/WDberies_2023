from typing import Iterator

import loguru
from sqlalchemy import desc
from sqlalchemy.orm import Session

from src.posts.item.models import Item
from src.repositories import BaseRepository
from src.specification import Specification
from src.exceptions import ItemNotFoundErorr


class ItemRepository(BaseRepository):

    def get(self, spec: Specification) -> Item:
        item = self.session.query(Item).filter(spec).one()
        if not item:
            raise ItemNotFoundErorr()    # change to ItemNotFindException
        return item

    def list(self, spec: Specification | None = None) -> list[Item]:

        if spec is None:
            return self.session.query(Item).order_by(desc(Item.point)).all()
        else:
            return self.session.query(Item).filter(spec).order_by(desc(Item.point)).all()

    def add(self, obj: Item) -> Item:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def update(self, obj: Item) -> Item:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def delete(self, obj: Item):
        self.session.delete(obj)
        self.session.commit()
