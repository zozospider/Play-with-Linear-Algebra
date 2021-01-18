from __future__ import annotations

from typing import Iterable


class Vector:

    def __init__(self, lst: Iterable) -> None:
        # >>> v = Vector([5, 2])
        self._values = list(lst)

    def __len__(self) -> int:
        """返回向量长度 (有多少个元素)"""
        return len(self._values)

    def __getitem__(self, index: int) -> object:
        """取向量的第 index 个元素"""
        return self._values[index]

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
