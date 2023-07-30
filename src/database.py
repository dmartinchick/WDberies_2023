from contextlib import contextmanager, AbstractContextManager
from typing import Any
from src.config import logger

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, scoped_session, sessionmaker


class Base(DeclarativeBase):
    pass


class Database:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(url=db_url, echo=True)
        self._session_factory = scoped_session(sessionmaker(bind=self._engine))

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Any | AbstractContextManager[Session]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rolback because of exeption")
            session.rollback()
            raise
        finally:
            session.close()
