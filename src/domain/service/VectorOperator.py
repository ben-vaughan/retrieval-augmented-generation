import math
from typing import List


class VectorOperator:
    @classmethod
    def magnitude(
        cls,
        x: List[float]
    ) -> float:
        squared_sum = 0

        for i in x:
            i_squared = i * i
            squared_sum += i_squared

        return math.sqrt(squared_sum)

    @classmethod
    def dot_product(
        cls,
        x: List[float], 
        y: List[float],
    ) -> float:
        if len(x) != len(y):
            raise ValueError("Vectors must be of equal length.")

        result = 0.0
        for x2, y2 in zip(x, y):
            result += x2 * y2

        return result

    @classmethod
    def cosine_similarity(
        cls,
        x: List[float],
        y: List[float],
    ) -> float:
        if len(x) != len(y):
            raise ValueError("Vectors must be of equal length.")

        x_magnitude = cls.magnitude(x)
        y_magnitude = cls.magnitude(y)

        xy_magnitude = x_magnitude * y_magnitude
        if xy_magnitude == 0:
            return 0.0

        xy_dot_product = cls.dot_product(x, y)

        return (xy_dot_product / (xy_magnitude))