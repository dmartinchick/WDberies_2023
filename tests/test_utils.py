import loguru
import pytest
from src.posts.item.schemas import Item as ItemSchemas
from src.posts.utils import Elo
from src.exceptions import WrongTypeError


class TestPositiveElo:

    @pytest.mark.parametrize("winer_points, loser_points, expected",
                             [
                                 (400.0, 400.0, {"winer": 410.0, "loser": 390.0}),
                                 (410.0, 390.0, {"winer": 419.4, "loser": 380.6}),
                                 (0, 400.0, {"winer": 18.2, "loser": 381.8}),
                                 (0, 0, {"winer": 10, "loser": -10}),
                                 (400, 400.0, {"winer": 410.0, "loser": 390.0}),
                             ])
    def test_elo(self, winer_points: float, loser_points: float, expected: dict):
        elo = Elo(winer_points, loser_points)
        result = elo.calculate()
        assert result == expected


class TestNegativeElo:

    @pytest.mark.parametrize("winer_points, loser_points, expected_error",
                             [
                                 (400.0, "str", WrongTypeError),
                                 (400, "str", WrongTypeError),
                                 ("400", 400.0, WrongTypeError),
                                 ("400", "400.0", WrongTypeError),
                             ])
    def test_elo(self, winer_points: float, loser_points: float, expected_error):
        with pytest.raises(expected_error):
            elo = Elo(winer_points, loser_points)
            loguru.logger.info(elo.calculate())
