from contextlib import contextmanager, AbstractContextManager
from src.config import logger, config

from fastapi import Depends

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, scoped_session, sessionmaker

engine = create_engine(url=config.db.url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    except Exception:
        logger.exception("Session rolback because of exeption")
        session.rollback()
        raise
    finally:
        session.close()
