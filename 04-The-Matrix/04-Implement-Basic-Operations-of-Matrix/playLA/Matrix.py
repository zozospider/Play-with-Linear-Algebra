from __future__ import annotations

from typing import List

from .Vector import Vector


class Matrix:

    def __init__(self, list2d: List[List[float]]) -> None:
        # >>> matrix = Matrix([[1, 2], [3, 4]])
        self._values = [row[:] for row in list2d]

    @classmethod
    def zero(cls, r: int, c: int) -> Matrix:
        """返回一个 r 行 c 列的零矩阵"""
        return cls([[0] * c for _ in range(r)])

    def __getitem__(self, index: int) -> Vector:
        """返回矩阵 index 行的元素"""
        return Vector(self._values[index])

    def __setitem__(self, index: int, vector: Vector) -> None:
        """设置矩阵 index 行的元素为 vector"""
        self._values[index] = list(vector)

    def __add__(self, another: Matrix) -> Matrix:
        """返回两个矩阵的加法结果"""
        assert self.shape() == another.shape(), \
            "Error in adding. Shape of matrix must be same"
        # m = []
        # for i in range(self.row_num()):
        #     v = []
        #     for a, b in zip(self.row_vector(i), another.row_vector(i)):
        #         v.append(a + b)
        #     m.append(v)
        # return Matrix(m)
        return Matrix(
            [[a + b for a, b in zip(self.row_vector(i), another.row_vector(i))] for i in range(self.row_num())])

    def __sub__(self, another: Matrix) -> Matrix:
        """返回两个矩阵的减法结果"""
        assert self.shape() == another.shape(), \
            "Error in subtracting. Shape of matrix must be same"
        # m = []
        # for i in range(self.row_num()):
        #     v = []
        #     for a, b in zip(self.row_vector(i), another.row_vector(i)):
        #         v.append(a - b)
        #     m.append(v)
        # return Matrix(m)
        return Matrix(
            [[a - b for a, b in zip(self.row_vector(i), another.row_vector(i))] for i in range(self.row_num())])

    def __mul__(self, k: float) -> Matrix:
        """返回矩阵的数量乘结果: self * k"""
        # m = []
        # for i in range(self.row_num()):
        #     v = []
        #     for e in self.row_vector(i):
        #         v.append(e * k)
        #     m.append(v)
        # return Matrix(m)
        return Matrix([[e * k for e in self.row_vector(i)] for i in range(self.row_num())])

    def __rmul__(self, k: float) -> Matrix:
        """返回矩阵的数量乘结果: k * self"""
        return self * k

    def __truediv__(self, k: float) -> Matrix:
        """返回数量除法的结果矩阵: self / k"""
        return self * (1 / k)

    def __pos__(self) -> Matrix:
        """返回矩阵取正的结果"""
        return self * 1

    def __neg__(self) -> Matrix:
        """返回矩阵取负的结果"""
        return self * -1

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
