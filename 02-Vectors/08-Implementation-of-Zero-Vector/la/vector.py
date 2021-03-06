from __future__ import annotations

from typing import Iterable, List


class Vector:

    def __init__(self, lst: List[float]) -> None:
        # >>> v = Vector([5, 2])
        self._values = list(lst)

    @classmethod
    def zero(cls, dim: int) -> Vector:
        """返回一个 dim 维的零向量"""
        return cls([0] * dim)

    def __len__(self) -> int:
        """返回向量长度 (有多少个元素)"""
        return len(self._values)

    def __getitem__(self, index: int) -> float:
        """取向量的第 index 个元素"""
        return self._values[index]

    def __iter__(self) -> Iterable:
        """返回向量的迭代器"""
        # 实现了该方法, 表示此对象是可迭代的
        return self._values.__iter__()

    def __add__(self, another: Vector) -> Vector:
        """向量加法, 返回结果向量"""
        assert len(self) == len(another), \
            "Error in adding, Length of vectors must be same"
        # return Vector([a + b for a, b in zip(self._values, another._values)])
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another: Vector) -> Vector:
        """向量减法, 返回结果向量"""
        assert len(self) == len(another), \
            "Error in subtracting, Length of vectors must be same"
        # return Vector([a - b for a, b in zip(self._values, another._values)])
        return Vector([a - b for a, b in zip(self, another)])

    def __mul__(self, k: float) -> Vector:
        """返回数量乘法的结果向量: self * k"""
        return Vector([k * e for e in self])

    def __rmul__(self, k: float) -> Vector:
        """返回数量乘法的结果向量: k * self"""
        return self * k

    def __truediv__(self, k: float) -> Vector:
        """返回数量除法的结果向量: self / k"""
        return self * (1 / k)

    def __pos__(self) -> Vector:
        """返回向量取正的结果向量"""
        return self * 1

    def __neg__(self) -> Vector:
        """返回向量取负的结果向量"""
        return self * -1

    def __repr__(self) -> str:
        # >>> v = Vector([5, 2])
        # >>> v
        # Vector([5, 2])
        return "Vector({})".format(self._values)

    def __str__(self) -> str:
        # >>> v = Vector([5, 2])
        # >>> print(v)
        # [5, 2]
        # return "({})".format(", ".join(str(e) for e in self._values))
        return str(self._values)
