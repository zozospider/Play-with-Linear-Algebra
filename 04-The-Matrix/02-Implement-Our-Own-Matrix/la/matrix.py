from __future__ import annotations

from typing import List

from .vector import Vector


class Matrix:

    def __init__(self, list2d: List[List[float]]) -> None:
        # >>> matrix = Matrix([[1, 2], [3, 4]])
        self._values = [row[:] for row in list2d]

    def __getitem__(self, index: int) -> Vector:
        """返回矩阵 index 行的元素"""
        return Vector(self._values[index])

    def __setitem__(self, index: int, vector: Vector) -> None:
        """设置矩阵 index 行的元素为 vector"""
        self._values[index] = list(vector)

    def __repr__(self) -> str:
        return "Matrix({})".format(self._values)

    # __str__ = __repr__

    def __str__(self) -> str:
        return str(self._values)

    def shape(self) -> tuple:
        """返回矩阵的形状: (行数, 列数)"""
        return len(self._values), len(self._values[0])

    def row_num(self) -> int:
        """返回矩阵的行数"""
        return self.shape()[0]

    __len__ = row_num

    def col_num(self) -> int:
        """返回矩阵的列数"""
        return self.shape()[1]

    def size(self) -> int:
        """返回矩阵的元素个数"""
        r, c = self.shape()
        return r * c

    def row_vector(self, index: int) -> Vector:
        """返回矩阵的第 index 个行向量"""
        return Vector(self._values[index])

    def col_vector(self, index: int) -> Vector:
        """返回矩阵的第 index 个列向量"""
        return Vector([row[index] for row in self._values])
