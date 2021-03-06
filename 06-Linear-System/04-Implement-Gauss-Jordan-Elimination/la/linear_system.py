from .matrix import Matrix
from .vector import Vector
from ._globals import is_equal
from ._globals import is_zero


class LinearSystem:
    """限定为 n 个未知数, n 个方程, 且有唯一解的情况"""

    # 线性方程              系数矩阵       增广矩阵           消元后的矩阵
    #      4y + 8z = 2    [ 0 4 8 ]    [ 0 4 8 | 2 ]    [ 1 0 0 |  2   ]
    # 2x + 2y +  z = 2    [ 2 2 1 ]    [ 2 2 1 | 2 ]    [ 0 1 0 | -1.5 ]
    # 4x + 8y + 8z = 4    [ 4 8 8 ]    [ 4 8 8 | 4 ]    [ 0 0 1 |  1   ]
    #
    # matrix       vector   augmented_matrix   augmented_matrix (after gauss_jordan_elimination)
    # [ 0 4 8 ]    [ 2 ]    [ 0 4 8 2 ]        [ 1 0 0  2   ]
    # [ 2 2 1 ]    [ 2 ]    [ 2 2 1 2 ]        [ 0 1 0 -1.5 ]
    # [ 4 8 8 ]    [ 4 ]    [ 4 8 8 4 ]        [ 0 0 1  1   ]
    def __init__(self, matrix: Matrix, vector: Vector) -> None:
        assert matrix.row_num() == len(vector), \
            "row number of matrix must be equal to the length of vector"
        assert matrix.row_num() == matrix.col_num(), \
            "row number of matrix must be equal to col number of matrix"
        # 系数矩阵的行列数
        self._n = matrix.row_num()
        # 增广矩阵
        # self.augmented_matrix = [Vector(matrix.row_vector(i).underlying_list() + [vector[i]]) for i in range(self._n)]
        self.augmented_matrix = Matrix([matrix.row_vector(i).underlying_list() + [vector[i]] for i in range(self._n)])

    def gauss_jordan_elimination(self) -> None:
        """执行高斯消元法"""
        # 前向过程 (从上到下)
        self._forward()
        # 后向过程 (从下到上)
        self._backward()

    def _forward(self) -> None:
        """
        前向过程 (从上到下)

        对从上到下每一行执行以下操作:
            step a: 判断当前行的主元 (第 r 行, 第 r 列) 是否为 0, 如果为 0, 则将下面的具有最大值主元的行与当前行交换
            step b: 将当前行的主元 (第 r 行, 第 r 列) 化为 1
            step c: 主元下面的所有行减去主元所在行的某个倍数, 使得主元 (第 r 行, 第 r 列) 下面所有元素都为 0
        """
        # r = 0
        # row 1 - step a:
        # [ 0 4 8 | 2 ]    [ 4 8 8 | 4 ]
        # [ 2 2 1 | 2 ] => [ 2 2 1 | 2 ]
        # [ 4 8 8 | 4 ]    [ 0 4 8 | 2 ]
        # row 1 - step b:
        # [ 4 8 8 | 4 ]    [ 1 2 2 | 1 ]
        # [ 2 2 1 | 2 ] => [ 2 2 1 | 2 ]
        # [ 0 4 8 | 2 ]    [ 0 4 8 | 2 ]
        # row 1 - step c:
        # [ 1 2 2 | 1 ]    [ 1  2  2 | 1 ]
        # [ 2 2 1 | 2 ] => [ 0 -2 -3 | 0 ]
        # [ 0 4 8 | 2 ]    [ 0  4  8 | 2 ]
        #
        # r = 1
        # row 2 - step a: ignore
        # row 2 - step b:
        # [ 1  2  2 | 1 ]    [ 1 2 2   | 1 ]
        # [ 0 -2 -3 | 0 ] => [ 0 1 1.5 | 0 ]
        # [ 0  4  8 | 2 ]    [ 0 4 8   | 2 ]
        # row 2 - step c:
        # [ 1 2 2   | 1 ]    [ 1 2 2   | 1 ]
        # [ 0 1 1.5 | 0 ] => [ 0 1 1.5 | 0 ]
        # [ 0 4 8   | 2 ]    [ 0 0 2   | 2 ]
        #
        # r = 2
        # row 3 - step a: ignore
        # row 3 - step b:
        # [ 1 2 2   | 1 ]    [ 1 2 2   | 1 ]
        # [ 0 1 1.5 | 0 ] => [ 0 1 1.5 | 0 ]
        # [ 0 0 2   | 2 ]    [ 0 0 1   | 1 ]
        # row 3 - step c: ignore

        # loop rows
        for r in range(self._n):
            # step a
            if is_zero(self.augmented_matrix[r][r]):
                max_row_below = self._max_row_below(r)
                self._swap_row(r, max_row_below)
            # step b
            if not is_equal(self.augmented_matrix[r][r], 1):
                self.augmented_matrix[r] = self.augmented_matrix[r] / self.augmented_matrix[r][r]
            # step c
            for r_below in range(r + 1, self._n):
                multiples_of_row_i = self.augmented_matrix[r_below][r]
                if not is_zero(multiples_of_row_i):
                    self.augmented_matrix[r_below] = self.augmented_matrix[r_below] \
                                                     - multiples_of_row_i * self.augmented_matrix[r]

    def _backward(self) -> None:
        """
        后向过程 (从下到上)

        对从下到上 (从倒数第一行开始, 到第二行结束) 每一行执行以下操作:
            主元上面的所有行减去主元所在行的某个倍数, 使得主元 (第 r 行, 第 r 列) 上面所有元素都为 0
        """
        # r = 2
        # row -1:
        # [ 1 2 2   | 1 ]    [ 1 2 0 | -1   ]
        # [ 0 1 1.5 | 0 ] => [ 0 1 0 | -1.5 ]
        # [ 0 0 1   | 1 ]    [ 0 0 1 |  1   ]
        #
        # r = 1
        # row -2:
        # [ 1 2 0 | -1   ]    [ 1 0 0 |  2   ]
        # [ 0 1 0 | -1.5 ] => [ 0 1 0 | -1.5 ]
        # [ 0 0 1 |  1   ]    [ 0 0 1 |  1   ]

        # loop rows
        for r in range(self._n - 1, 0, -1):
            for r_above in range(r - 1, -1, -1):
                multiples_of_row_i = self.augmented_matrix[r_above][r]
                if not is_zero(multiples_of_row_i):
                    self.augmented_matrix[r_above] = self.augmented_matrix[r_above] \
                                                     - multiples_of_row_i * self.augmented_matrix[r]

    def _max_row_below(self, r: int) -> int:
        """返回当前行的下面所有行中具有最大主元的行"""
        # 初始化具有最大主元的行为当前行, 最大主元为当前行的主元
        max_row = r
        max_value = abs(self.augmented_matrix[r][r])
        # 遍历 r 行的下面所有行
        for i in range(r + 1, self._n):
            if abs(self.augmented_matrix[i][i]) > max_value:
                max_row = i
                max_value = self.augmented_matrix[i][i]
        return max_row

    def _swap_row(self, r1: int, r2: int) -> None:
        """交换当前增广矩阵中的两行"""
        self.augmented_matrix[r1], self.augmented_matrix[r2] = self.augmented_matrix[r2], self.augmented_matrix[r1]

    def augmented_matrix_fancy_print(self) -> None:
        """打印当前增广矩阵"""
        for i in range(self._n):
            print(" ".join(str(self.augmented_matrix[i][j]) for j in range(self._n)), end=" ")
            print("|", self.augmented_matrix[i][-1])
