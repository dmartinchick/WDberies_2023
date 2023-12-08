import loguru

from src.posts.item.models import Item as ItemModels


data_for_test = [
    ItemModels(
        brand="tets_brand",
        img_url="http://test_url.com",
        is_active=True,
        name="test_name",
        price=1500.0),
    ItemModels(
        brand="some_brand",
        img_url=None,
        is_active=True,
        name="some_name",
        price=100.0),
    ItemModels(
        brand="super_brand",
        img_url="http://super_url.com",
        is_active=True,
        name="super_name"),
    ItemModels(
        brand="puper_brand",
        img_url="http://puper_url.com",
        is_active=True,
        name="puper_name",
        point=1000.0,
        price=1500.0),
    ItemModels(
        brand="false_brand",
        img_url="http://false_url.com",
        is_active=False,
        name="false_name")
]


class TData:

    def __init__(self, data: list[ItemModels]):
        self.data = data
        self.is_active_counter = self.__is_active_counter()
        self.is_inactive_counter = self.__is_inactive_counter()
        self.item_counter = self.__item_counter()

    def __is_active_counter(self) -> int:
        counter = 0
        for item in self.data:
            if item.is_active is True:
                counter += 1
        return counter

    def __is_inactive_counter(self) -> int:
        counter = 0
        for item in self.data:
            if item.is_active is False:
                counter += 1
        return counter

    def __item_counter(self) -> int:
        return len(self.data)


test_data = TData(data_for_test)
