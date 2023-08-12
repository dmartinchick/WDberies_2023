from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from typing import Iterator, Any

from fastapi import Depends

from sqlalchemy.orm import Session

from src.specification import Specification
from src.database import Database


class BaseRepository(ABC):

    def __init__(self, session_factory: Any | AbstractContextManager[Session] = Depends(Database)):
        self.session_factory = session_factory

    @abstractmethod
    def get(self, spec: Specification) -> Any:
        raise NotImplementedError

    @abstractmethod
    def list(self, spec: Specification | None = None) -> Iterator:
        raise NotImplementedError

    @abstractmethod
    def add(self, obj: Any):
        raise NotImplementedError

    @abstractmethod
    def update(self, obj: Any):
        raise NotImplementedError

    @abstractmethod
    def delete(self, obj: Any):
        raise NotImplementedError
