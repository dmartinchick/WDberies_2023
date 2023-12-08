from math import pow
from enum import Enum
import loguru

from src.exceptions import WrongTypeError
from src.posts.item.schemas import Result


class Elo:

    def __init__(self, item_a_points: float, item_b_points: float):
        self.item_a_points = item_a_points
        self.item_b_points = item_b_points
        self.k_for_item_a = self.__choose_k(self.item_a_points)
        self.k_for_item_b = self.__choose_k(self.item_b_points)
        self.__expected_points = self.__calculate_expected_points()

    @property
    def item_a_points(self) -> float:
        return self.__a_points

    @item_a_points.setter
    def item_a_points(self, points):
        if isinstance(points, float | int):
            self.__a_points = float(points)
        else:
            raise WrongTypeError()

    @property
    def item_b_points(self) -> float:
        return self.__b_points

    @item_b_points.setter
    def item_b_points(self, points):
        if isinstance(points, float | int):
            self.__b_points = points
        else:
            raise WrongTypeError()

    @staticmethod
    def __choose_k(item_points: float) -> int:
        return 10 if item_points >= 2400 else 20

    def __calculate_expected_points(self) -> dict:
        expected_points_item_a = 1/(1 + pow(10, (self.__b_points - self.__a_points) / 400))
        expected_points_item_b = 1/(1 + pow(10, (self.__a_points - self.__b_points) / 400))

        return {"item_a": expected_points_item_a, "item_b": expected_points_item_b}

    @staticmethod
    def distribute_points(result: Result):
        if result.value == "item_a":
            return 1.0, 0
        elif result.value == "draw":
            return 0.5, 0.5
        else:
            return 0, 1.0

    def calculate(self, result: Result) -> dict:
        Sa, Sb = self.distribute_points(result)
        new_points_item_a = self.__a_points + self.k_for_item_a * (Sa - self.__expected_points.get("item_a"))

        new_points_item_b = self.__b_points + self.k_for_item_b * (Sb - self.__expected_points.get("item_b"))
        return {"item_a": round(new_points_item_a, 1), "item_b": round(new_points_item_b, 1)}
