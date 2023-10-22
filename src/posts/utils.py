from math import pow
import loguru

from src.exceptions import WrongTypeError


class Elo:

    def __init__(self, winer_points: float, loser_points: float):
        self.winer_points = winer_points
        self.loser_points = loser_points
        self.k_for_winer = self.__choose_k(self.winer_points)
        self.k_for_loser = self.__choose_k(self.loser_points)
        self.expected_points = self.__calculate_expected_points()

    @property
    def winer_points(self) -> float:
        return self.__winer_points

    @winer_points.setter
    def winer_points(self, points):
        if isinstance(points, float | int):
            self.__winer_points = float(points)
        else:
            raise WrongTypeError()

    @property
    def loser_points(self) -> float:
        return self.__loser_points

    @loser_points.setter
    def loser_points(self, points):
        if isinstance(points, float | int):
            self.__loser_points = points
        else:
            raise WrongTypeError()

    @staticmethod
    def __choose_k(item_points: float) -> int:
        return 10 if item_points >= 2400 else 20

    def __calculate_expected_points(self) -> dict:
        expected_points_winer = 1/(1 + pow(10, (self.__loser_points - self.__winer_points) / 400))
        expected_points_loser = 1/(1 + pow(10, (self.__winer_points - self.__loser_points) / 400))

        return {"winer": expected_points_winer, "loser": expected_points_loser}

    def calculate(self) -> dict:
        new_points_winer = self.__winer_points + self.k_for_winer * (1 - self.expected_points.get("winer"))
        new_points_loser = self.__loser_points + self.k_for_loser * (0 - self.expected_points.get("loser"))
        return {"winer": round(new_points_winer, 1), "loser": round(new_points_loser, 1)}
