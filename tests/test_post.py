import pytest
import random

from src.config import logger
from src.app import app
from src.posts.item.schemas import Item as ItemShema
from tests.conftest import client_test, prepare_database, prepare_database_without_data
from tests.data_for_test import test_data


class TestPositivePost:
    def test_status(self, client_test, prepare_database):
        responce = client_test.get("/status")
        assert responce.status_code == 200
        data = responce.json()
        assert data == {'status': "Ok"}

    def test_get_all_items(self, client_test):
        responce = client_test.get("/items")
        data = responce.json()
        assert responce.status_code == 200
        assert len(data) == test_data.item_counter

    def test_get_random_items(self, client_test):
        responce = client_test.get("/items_random/")
        data = responce.json()
        assert responce.status_code == 200
        assert isinstance(data, list)
        assert isinstance(data[0], dict) and isinstance(data[1], dict)
        assert len(data) == 2
        assert data[0] != data[1]
        assert data[0].get('img_url') is not None
        assert data[1].get('img_url') is not None

    def test_get_all_active_items(self, client_test):
        responce = client_test.get("/items_is_active")
        data = responce.json()
        assert responce.status_code == 200
        assert len(data) == test_data.is_active_counter

    def test_get_all_inactive_items(self, client_test):
        responce = client_test.get("/items_is_not_active/")
        data = responce.json()
        assert responce.status_code == 200
        assert len(data) == test_data.is_inactive_counter

    def test_get_item_by_id(self, client_test):
        # random_int = random.randint(1, test_data.item_counter)
        responce = client_test.get("/items/item_id", params={"item_id": 1})
        data = responce.json()
        assert responce.status_code == 200
        assert isinstance(data, dict)

    def test_create_item(self, client_test):
        responce = client_test.post(
            url="/items/",
            json={"id": 100, "brand": "added_brand", "img_url": "http://added.com",
                  "name": "i'm added", "price": 500.0})
        assert responce.status_code == 200
        responce_check = client_test.get("/items/item_id", params={"item_id": 100})
        assert responce_check.status_code == 200
        assert responce_check.json() == {"id": 100,
                                         "brand": "added_brand",
                                         "img_url": "http://added.com",
                                         "name": "i'm added",
                                         "is_active": True,
                                         "point": 400.0,
                                         "price": 500.0}

#
# class TestNegativePost:
#     def test_get_all_items(self, client_test, prepare_database_without_data):
#         responce = client_test.get("/items")
#         data = responce.json()
#         assert data == []
#
#     def test_get_random_items(self, client_test):
#         with pytest.raises(ValueError, match=r".* недостаточно элементов .*"):
#             responce = client_test.get("/items_random")
#             data = responce.json()
#             assert data == []
#
#     def test_get_item_by_id(self, client_test):
#         responce = client_test.get("/items{item_id}", params={'item_id': 0})
#         data = responce.json()
#         assert isinstance(data, dict)
#         assert len(data) == 1
    #
    # def test_get_all_active_items(self, client_test):
    #     responce = client_test.get("/items_is_active")
    #     data = responce.json()
    #     assert len(data) == 4
