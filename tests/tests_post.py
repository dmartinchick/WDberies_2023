from unittest import mock

import pytest
from fastapi.testclient import TestClient

from src.posts.item.repositories import ItemRepository
from src.exceptions import ItemNotFoundErorr
from src.posts.item.schemas import Item
from src.app import app


@pytest.fixture
def client():
    yield TestClient(app)


def test_status(client):
    responce = client.get("/status")
    assert responce.status_code == 200
    data = responce.json()
    assert data == {'status': "Ok"}


def test_get_list(client):
    repository_mock = mock.Mock(spec=ItemRepository)
    repository_mock.list.return_value = [
        Item(id=1, brand="test_brand", img_url="http://test_url.com", is_active=True,
             name="test_name", point=300.0, price=1000.0),
        Item(id=2, brand="super_puper", img_url="http://super_url.com", is_active=False,
             name="super_puper_name", point=700.1, price=10.0)
    ]

    with app.container.item_repository.override(repository_mock):
        responce = client.get('/items')

    assert responce.status_code == 200
    data = responce.json()
    assert data == [
        {'id': 1, 'brand': "test_brand", 'img_url': "http://test_url.com", 'is_active': True,
         'name': "test_name", 'point': 300.0, 'price': 1000.0},
        {'id': 2, 'brand': "super_puper", 'img_url': "http://super_url.com", 'is_active': False,
         'name': "super_puper_name", 'point': 700.1, 'price': 10.0}
    ]
