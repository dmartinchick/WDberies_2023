from typing import Iterator

from sqlalchemy import desc
from sqlalchemy.orm import Session

from src.posts.item.schemas import Item
from src.repositories import BaseRepository
from src.specification import Specification
from src.exceptions import ItemNotFoundErorr


class ItemRepository(BaseRepository):

    def get(self, spec: Specification) -> Item:
        with self.session_factory() as session:
            item = session.query(Item).filter(spec).one()
            if not item:
                raise ItemNotFoundErorr()    # change to ItemNotFindException
            return item

    def list(self, spec: Specification | None = None) -> Iterator:
        if spec is None:
            with self.session_factory() as session:
                return session.query(Item).order_by(desc(Item.point)).all()
        else:
            with self.session_factory() as session:
                return session.query(Item).filter(spec).order_by(desc(Item.point)).all()

    def add(self, obj: Item) -> Item:
        with self.session_factory() as session:
            session.add(obj)
            session.commit()
            session.refresh(obj)
            return obj

    def update(self, obj: Item) -> Item:
        with self.session_factory() as session:
            session.add(obj)
            session.commit()
            session.refresh(obj)
            return obj

    def delete(self, obj: Item):
        with self.session_factory() as session:
            session.delete(obj)
            session.commit()
