import requests
import re
from loguru import logger


class WBParser:
    def __init__(self, curl: str | None = None):
        self.curl = curl
        self.pices = self.curl

    @property
    def curl(self) -> str:
        return self.__curl

    @curl.setter
    def curl(self, curl: str | None):
        if isinstance(curl, str):
            self.pices = curl
            self.__curl = curl
        elif curl is None:
            self.__curl = None
        else:
            raise TypeError

    @property
    def pices(self) -> dict:
        return self.__pices

    @pices.setter
    def pices(self, curl: str):
        if curl is not None:
            self.__pices = self.__split_curl(curl)
        else:
            self.__pices = None

    @staticmethod
    def get_category(url: str) -> str:
        category = re.search("(?<=category=)[0-9]+", url)
        return category.group(0)

    @staticmethod
    def __split_curl(curl: str) -> dict:
        if curl is not None:
            return {
                "part_1": re.search(".+(?<=page=)", curl).group(0),
                "part_2": re.search("(?=&app).+", curl).group(0)
            }
        else:
            raise ValueError

    def __create_curl(self, page: int = 1) -> str:

        curl = f"{self.__pices.get('part_1')}{page}{self.__pices.get('part_2')}"
        return curl

    def get_responce(self, how_much_page: int = 1) -> list:
        res = []
        for page in range(1, how_much_page + 1):
            curl = self.__create_curl(page=page)
            logger.info(curl)
            data = requests.get(curl)
            data_json = data.json()
            cards = data_json.get("data").get("products")
            for card in cards:
                res.append(card)
        logger.info(f"counter items: {len(res)}")
        return res

    def resp(self):
        curl = self.__create_curl()
        data = requests.get(url=curl)
        info = data.json()
        return info


parser = WBParser()
# curl 'https://catalog.wb.ru/catalog/dresses/v1/catalog?cat=8137&limit=100&sort=popular&page=1&appType=128&curr=byn&lang=ru&dest=-59208&spp=27&f23796=31136&fcolor=16777215&TestGroup=no_test&TestID=no_test' \
#       https://www.wildberries.by/catalog?category=8137&f23796=31136&fcolor=16777215&page=1&sort=popular