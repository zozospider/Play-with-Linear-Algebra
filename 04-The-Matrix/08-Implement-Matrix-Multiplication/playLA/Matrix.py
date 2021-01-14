from .Vector import Vector


class Matrix:

    def __init__(self, list2d):
        # >>> matrix = Matrix([[1, 2], [3, 4]])
        self._values = [row[:] for row in list2d]

    @classmethod
    def zero(cls, r, c):
        """返回一个 r 行 c 列的零矩阵"""
        return cls([[0] * c for _ in range(r)])

    def __getitem__(self, pos):
        """返回矩阵 pos 位置的元素"""
        r, c = pos
        return self._values[r][c]

    def __add__(self, another):
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

    def __sub__(self, another):
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

    def __mul__(self, k):
        """返回矩阵的数量乘结果: self * k"""
        # m = []
        # for i in range(self.row_num()):
        #     v = []
        #     for e in self.row_vector(i):
        #         v.append(e * k)
        #     m.append(v)
        # return Matrix(m)
        return Matrix([e * k for e in self.row_vector(i)] for i in range(self.row_num()))

    def __rmul__(self, k):
        """返回矩阵的数量乘结果: k * self"""
        return self * k

    def __truediv__(self, k):
        """返回数量除法的结果矩阵: self / k"""
        return self * (1 / k)

    def __pos__(self):
        """返回矩阵取正的结果"""
        return self * 1

    def __neg__(self):
        """返回矩阵取负的结果"""
        return self * -1

    def __repr__(self):
        return "Matrix({})".format(self._values)

    # __str__ = __repr__

    def __str__(self):
        return str(self._values)

    def shape(self):
        """返回矩阵的形状: (行数, 列数)"""
        return len(self._values), len(self._values[0])

    def row_num(self):
        """返回矩阵的行数"""
        return self.shape()[0]

    __len__ = row_num

    def col_num(self):
        """返回矩阵的列数"""
        return self.shape()[1]

    def size(self):
        """返回矩阵的元素个数"""
        r, c = self.shape()
        return r * c

    def row_vector(self, index):
        """返回矩阵的第 index 个行向量"""
        return Vector(self._values[index])

    def col_vector(self, index):
        """返回矩阵的第 index 个列向量"""
        return Vector([row[index] for row in self._values])

    def dot(self, another):
        """返回矩阵乘法的结果"""
        if isinstance(another, Vector):
            # 矩阵和向量的乘法
            #     M(m*k)       V(k)      V(m)
            # [ - - r1 - - ]   [ | ]   [ r1.v ]
            # [ - - r2 - - ]   [ | ]   [ r2.v ]
            # [     ...    ] . [ v ] = [ ...  ]
            # [     ...    ]   [ | ]   [ ...  ]
            # [ - - rm - - ]   [ | ]   [ r4.v ]

            #    5*3        3       5
            # [ 1 2 0 ]           [ 4 ]
            # [ 2 1 5 ]   [ 2 ]   [ 5 ]
            # [ 1 1 2 ] . [ 1 ] = [ 3 ]
            # [ 1 0 0 ]   [ 0 ]   [ 2 ]
            # [ 4 1 2 ]           [ 9 ]
            assert self.col_num() == len(another), \
                "Error in Matrix-Vector Multiplication"
            return Vector([self.row_vector(i).dot(another) for i in range(self.row_num())])

        if isinstance(another, Matrix):
            # 矩阵和矩阵的乘法
            #     M(m*k)           M(k*n)                 M(m*n)
            # [ - - r1 - - ]   [ |  |      | ]   [ r1.c1 r1.c2 ... r1.cn ]
            # [ - - r2 - - ]   [ |  |      | ]   [ r2.c1 r2.c2 ... r2.cn ]
            # [     ...    ] . [ c1 c2 ... cn] = [  ...   ...       ...  ]
            # [     ...    ]   [ |  |      | ]   [  ...   ...       ...  ]
            # [ - - rm - - ]   [ |  |      | ]   [ rm.c1 rm.c2 ... rm.cn ]

            #    5*3        3*2       5*2
            # [ 1 2 0 ]             [ 4 6 ]
            # [ 2 1 5 ]   [ 2 0 ]   [ 5 8 ]
            # [ 1 1 2 ] . [ 1 3 ] = [ 3 5 ]
            # [ 1 0 0 ]   [ 0 1 ]   [ 2 0 ]
            # [ 4 1 2 ]             [ 9 5 ]
            assert self.col_num() == another.row_num(), \
                "Error in Matrix-Matrix Multiplication"
            # m = []
            # for i in range(self.row_num()):
            #     v = []
            #     for j in range(another.col_num()):
            #         v.append(self.row_vector(i).dot(another.col_vector(j)))
            #     m.append(v)
            # return Matrix(m)
            return Matrix([[self.row_vector(i).dot(another.col_vector(j)) for j in range(another.col_num())]
                           for i in range(self.row_num())])
