import requests
from loguru import logger


class WBParser:
    def __init__(self, user_url: str):
        self.url = user_url # https://www.wildberries.by/catalog?category=8137&f23796=31136%3B31142&fcolor=16777215&page=1&sort=popular
        self.__cURL = 'https://catalog.wb.ru/catalog/' \
                      'dresses/v1/' \
                      'catalog?' \
                      'cat=8137&' \
                      'limit=100&' \
                      'sort=popular&' \
                      'page=1&' \
                      'appType=128&' \
                      'curr=byn&' \
                      'lang=ru&' \
                      'dest=-59208&' \
                      'spp=27&' \
                      'f23796=31136;31142&' \
                      'fcolor=16777215&' \
                      'TestGroup=no_test&TestID=no_test'

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, user_url: str):
        if isinstance(user_url, str):
            self.__url = user_url
        else:
            raise TypeError

    def get_responce(self):
        res = requests.get(self.url)
        return res

    def __get_category(self):
        pass


parser = WBParser(
    user_url="https://www.wildberries.by/catalog?category=8137&f23796=31136%3B31142&fcolor=16777215&page=1&sort=popular"
)
