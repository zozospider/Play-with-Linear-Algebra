class Vector:

    def __init__(self, lst):
        # >>> v = Vector([5, 2])
        self._values = lst

    def __len__(self):
        """返回向量长度 (有多少个元素)"""
        return len(self._values)

    def __getitem__(self, index):
        """取向量的第 index 个元素"""
        return self._values[index]

    def __repr__(self):
        # >>> v = Vector([5, 2])
        # >>> v
        # Vector([5, 2])
        return "Vector({})".format(self._values)

    def __str__(self):
        # >>> v = Vector([5, 2])
        # >>> print(v)
        # (5, 2)
        return "({})".format(", ".join(str(e) for e in self._values))
