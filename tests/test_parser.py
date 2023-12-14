import pytest
from loguru import logger
from src.posts.utils.parser import parser, WBParser


class TestPositiveParser:

    def test_check_status_code(self):
        res = parser.get_responce()
        assert res.status_code == 200

    @pytest.mark.parametrize("curl, expected_result",
                             [
                                 ('https://www.wildberries.by/catalog?category=130421&page=1&sort=popular&xsubject=260', '130421'),
                                 ('https://www.wildberries.by/catalog?category=8137&f23796=31136%3B31142&fcolor=16777215&page=1&sort=popular', '8137'),
                                 ('https://www.wildberries.by/catalog?category=9990&page=1&sort=popular&xsubject=5858', '9990')
                             ])
    def test_get_category(self, curl, expected_result):
        curent_parser = WBParser(user_url=curl)
        category = curent_parser.get_category(url=curl)
        # logger.info(category)
        assert category == expected_result
