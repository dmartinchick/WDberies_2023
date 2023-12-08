from typing import Iterator

import loguru
from sqlalchemy import desc
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from src.posts.item.models import Item
from src.repositories import BaseRepository
from src.specification import Specification
from src.exceptions import ItemNotFoundException


class ItemRepository(BaseRepository):

    def get(self, spec: Specification) -> Item:
        try:
            item = self.session.query(Item).filter(spec).one()
        except NoResultFound:
            raise ItemNotFoundException()
        return item

    def list(self, spec: Specification | None = None) -> list[Item]:
        try:
            if spec is None:
                items = self.session.query(Item).order_by(desc(Item.point)).all()
            else:
                items = self.session.query(Item).filter(spec).order_by(desc(Item.point)).all()
        except NoResultFound:
            raise ItemNotFoundException()
        return items

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
