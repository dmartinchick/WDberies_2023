import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker, Session

from src.config import logger, config
from src.app import app
from src.database import Base, get_session
from src.posts.item.models import Item
from src.posts.item.repositories import ItemRepository
from tests.data_for_test import data_for_test


engine = create_engine(url=config.test_db.url)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_session() -> Session:
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


app.dependency_overrides[get_session] = override_get_session


@pytest.fixture(scope="class")
def prepare_database():
    Base.metadata.create_all(engine)
    fill_db(data_for_test)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="class")
def prepare_database_without_data():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


def fill_db(data):
    with TestingSessionLocal() as session:
        for item in data:
            session.add(item)
        session.commit()
        session.close()


@pytest.fixture
def client_test(prepare_database):
    yield TestClient(app)
