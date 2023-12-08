import pytest
from loguru import logger
from src.posts.utils.parser import parser


class TestPositiveParser:

    def test_check_status_code(self):
        res = parser.get_responce()
        assert res.status_code == 200
