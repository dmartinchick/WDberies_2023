import loguru
import pytest
from src.posts.item.schemas import Item as ItemSchemas, Result
from src.posts.utils import Elo
from src.exceptions import WrongTypeError


class TestPositiveElo:

    @pytest.mark.parametrize("item_a, item_b, result, expected",
                             [
                                 (400.0, 400.0, Result.ITEM_A_WIN, {"item_a": 410.0, "item_b": 390.0}),
                                 (410.0, 390.0, Result.ITEM_A_WIN, {"item_a": 419.4, "item_b": 380.6}),
                                 (400.0, 400.0, Result.ITEM_B_WIN, {"item_a": 390.0, "item_b": 410.0}),
                                 (2405.0, 50.0, Result.ITEM_B_WIN, {"item_a": 2395.0, "item_b": 70.0}),
                                 (2405.0, 3500.0, Result.DRAW, {"item_a": 2410.0, "item_b": 3495.0}),
                             ])
    def test_elo(self, item_a: float, item_b: float, result: Result, expected: dict):
        elo = Elo(item_a_points=item_a, item_b_points=item_b)
        result = elo.calculate(result)
        assert result == expected


class TestNegativeElo:

    @pytest.mark.parametrize("item_a, item_b, expected_error",
                             [
                                 (400.0, "str", WrongTypeError),
                                 (400, "str", WrongTypeError),
                                 ("400", 400.0, WrongTypeError),
                                 ("400", "400.0", WrongTypeError),
                             ])
    def test_elo(self, item_a: float, item_b: float, expected_error):
        with pytest.raises(expected_error):
            elo = Elo(item_a_points=item_a, item_b_points=item_b)
            loguru.logger.info(elo)
