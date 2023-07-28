from abc import ABC, abstractmethod
from typing import Iterator, Any
from repositories import BaseRepository


class BaseServices(ABC):
    def __init__(self, repository: BaseRepository) -> None:
        self._repository: BaseRepository = repository
