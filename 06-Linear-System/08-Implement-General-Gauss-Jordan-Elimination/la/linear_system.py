from .matrix import Matrix
from .vector import Vector
from ._globals import is_equal
from ._globals import is_zero


class LinearSystem:
    """不限定未知数个数, 方程个数, 在不同情况下可能有不同解"""

    # 不同情况下线性方程组解的情况
    #
    # 结论一 (R1)
    # R1-a: 方程个数 < 未知数个数: 无解 / 无数解
    # 如下 2 个方程 < 3 个未知数 (3 维):
    #  _ _           _ _
    # |  _|_      _/_   /
    # | | | |   | /  | /
    # |_|_| |   |/___|/
    #   |_ _|   | _ _|
    #
    # R1-b: 方程个数 = 未知数个数: 无解 / 唯一解 / 无数解
    # 如下 2 个方程 = 2 个未知数 (2 维):
    #    / /   \  /
    #   / /     \/
    #  / /      /\
    # / /      /  \
    #
    # R1-c: 方程个数 > 未知数个数: 无解 / 唯一解 / 无数解
    # 如下 3 个方程 > 2 个未知数 (2 维):
    #    / / /     \/ /   \ | /
    #   / / /      /\/     \|/
    #  / / /      / /\     /|\
    # / / /      / /  \   / | \
    #
    #
    # 结论二 (R2)
    # R2-a: 行最简形式 matrix 非零行 < 行最简形式 augmented_matrix 非零行: 无解
    # [ 1 0 0 | c1 ]
    # [ 0 1 0 | c2 ]
    # [ 0 1 0 | c3 ]
    # [ 0 0 0 | c4 ]
    #
    # R2-b: 行最简形式 matrix 非零行 < 未知数个数: 无数解
    # [ 1 0 0 0 | c1 ]
    # [ 0 0 1 0 | c2 ]
    # [ 0 0 0 1 | c3 ]
    # [ 0 0 0 0 | 0  ]
    #
    # R2-c: 行最简形式 matrix 非零行 = 未知数个数: 唯一解
    # [ 1 0 0 | c1 ]
    # [ 0 1 0 | c2 ]
    # [ 0 0 1 | c3 ]
    # [ 0 0 0 | 0  ]
    #
    #
    # 线性方程                       系数矩阵               增广矩阵                    消元后的矩阵
    #   x -y  +2z     +3u =  1     [  1 -1  2  0  3 ]    [  1 -1  2  0  3 |  1  ]    [ 1 -1 0 -2 0 | -15 ]
    #  -x +y      +2w -5u =  5     [ -1  1  0  2 -5 ]    [ -1  1  0  2 -5 |  5  ]    [ 0  0 1  1 0 |  5  ]
    #   x -y  +4z +2w +4u =  13    [  1 -1  4  2  4 ]    [  1 -1  4  2  4 |  13 ]    [ 0  0 0  0 1 |  2  ]
    # -2x +2y -5z  -w -3u = -1     [ -2  2 -5 -1 -3 ]    [ -2  2 -5 -1 -3 | -1  ]    [ 0  0 0  0 0 |  0  ]
    #
    # matrix               vector     augmented_matrix         augmented_matrix (after gauss_jordan_elimination)
    # [  1 -1  2  0  3 ]    [  1  ]    [  1 -1  2  0  3  1  ]    [ 1 -1 0 -2 0 -15 ]
    # [ -1  1  0  2 -5 ]    [  5  ]    [ -1  1  0  2 -5  5  ]    [ 0  0 1  1 0  5  ]
    # [  1 -1  4  2  4 ]    [  13 ]    [  1 -1  4  2  4  13 ]    [ 0  0 0  0 1  2  ]
    # [ -2  2 -5 -1 -3 ]    [ -1  ]    [ -2  2 -5 -1 -3 -1  ]    [ 0  0 0  0 0  0  ]
    def __init__(self, matrix: Matrix, vector: Vector) -> None:
        assert matrix.row_num() == len(vector), \
            "row number of matrix must be equal to the length of vector"
        # 系数矩阵的行数和列数
        self._m = matrix.row_num()
        self._n = matrix.col_num()
        # 增广矩阵
        # self.augmented_matrix = [matrix.row_vector(i).underlying_list() + [vector[i]] for i in range(self._m)]
        # self.augmented_matrix = [Vector(matrix.row_vector(i).underlying_list() + [vector[i]]) for i in range(self._m)]
        self.augmented_matrix = Matrix([matrix.row_vector(i).underlying_list() + [vector[i]] for i in range(self._m)])
        # 记录主元位置 (augmented_matrix 中每一行的主元在第几列)
        # [ 0,
        #   2,
        #   4 ]
        self.pivots = []

    def gauss_jordan_elimination(self) -> Matrix:
        """执行高斯消元法"""
        # 前向过程 (从上到下)
        self._forward()
        # 后向过程 (从下到上)
        self._backward()

        return self.augmented_matrix

    def _forward(self) -> None:
        """
        前向过程 (从上到下)

        对从上到下每一行执行以下操作:
            step a: 判断当前行的主元 (第 r 行, 第 c 列) 是否为 0, 如果为 0, 则将下面的具有非零的最大值主元 (轮询列直到主元非零) 的行与当前行交换
            step b: 将当前行的主元 (第 r 行, 第 c 列) 化为 1
            step c: 主元下面的所有行减去主元所在行的某个倍数, 使得主元 (第 r 行, 第 c 列) 下面所有元素都为 0
        """
        # r = 0
        # c = 0
        #
        # row 1 - step a: ignore
        # row 1 - step b: ignore
        # row 1 - step c:
        # [  1 -1  2  0  3 |  1  ]    [ 1 -1  2  0  3 | 1  ]
        # [ -1  1  0  2 -5 |  5  ] => [ 0  0  2  2 -2 | 6  ]
        # [  1 -1  4  2  4 |  13 ]    [ 0  0  2  2  1 | 12 ]
        # [ -2  2 -5 -1 -3 | -1  ]    [ 0  0 -1 -1  3 | 1  ]
        # r = 1
        # c = 1
        #
        # row 2 - step a:
        # [ 1 -1  2  0  3 | 1  ] c = 2 [ 1 -1  2  0  3 | 1  ]
        # [ 0  0  2  2 -2 | 6  ] =>    [ 0  0  2  2 -2 | 6  ]
        # [ 0  0  2  2  1 | 12 ]       [ 0  0  2  2  1 | 12 ]
        # [ 0  0 -1 -1  3 | 1  ]       [ 0  0 -1 -1  3 | 1  ]
        # row 2 - step b:
        # [ 1 -1  2  0  3 | 1  ]    [ 1 -1  2  0  3 | 1  ]
        # [ 0  0  2  2 -2 | 6  ] => [ 0  0  1  1 -1 | 3  ]
        # [ 0  0  2  2  1 | 12 ]    [ 0  0  2  2  1 | 12 ]
        # [ 0  0 -1 -1  3 | 1  ]    [ 0  0 -1 -1  3 | 1  ]
        # row 2 - step c:
        # [ 1 -1  2  0  3 | 1  ]    [ 1 -1 2 0  3 | 1 ]
        # [ 0  0  1  1 -1 | 3  ] => [ 0  0 1 1 -1 | 3 ]
        # [ 0  0  2  2  1 | 12 ]    [ 0  0 0 0  3 | 6 ]
        # [ 0  0 -1 -1  3 | 1  ]    [ 0  0 0 0  2 | 4 ]
        # r = 2
        # c = 3
        #
        # row 3 - step a: ignore
        # row 3 - step b:
        # [ 1 -1 2 0  3 | 1 ]    [ 1 -1 2 0  3 | 1 ]
        # [ 0  0 1 1 -1 | 3 ] => [ 0  0 1 1 -1 | 3 ]
        # [ 0  0 0 0  3 | 6 ]    [ 0  0 0 0  1 | 2 ]
        # [ 0  0 0 0  2 | 4 ]    [ 0  0 0 0  2 | 4 ]
        # row 3 - step c:
        # [ 1 -1 2 0  3 | 1 ]    [ 1 -1 2 0  3 | 1 ]
        # [ 0  0 1 1 -1 | 3 ] => [ 0  0 1 1 -1 | 3 ]
        # [ 0  0 0 0  1 | 2 ]    [ 0  0 0 0  1 | 2 ]
        # [ 0  0 0 0  2 | 4 ]    [ 0  0 0 0  0 | 0 ]
        # r=3
        # c=4
        #
        # row 4 - step a:
        # [ 1 -1 2 0  3 | 1 ] c = 5 [ 1 -1 2 0  3 | 1 ]
        # [ 0  0 1 1 -1 | 3 ] =>    [ 0  0 1 1 -1 | 3 ]
        # [ 0  0 0 0  1 | 2 ]       [ 0  0 0 0  1 | 2 ]
        # [ 0  0 0 0  0 | 0 ]       [ 0  0 0 0  0 | 0 ]
        # end

        # 定义行和列循环变量
        r = 0
        c = 0
        # loop rows
        while r < self._m and c < self._n:
            # step a
            if is_zero(self.augmented_matrix[r][c]):
                max_row_below = self._max_row_below(r, c)
                if is_zero(self.augmented_matrix[max_row_below][c]):
                    c += 1
                    continue
                else:
                    self._swap_row(r, max_row_below)
            # step b
            if not is_equal(self.augmented_matrix[r][c], 1):
                self.augmented_matrix[r] = self.augmented_matrix[r] / self.augmented_matrix[r][c]
            # step c
            for r_below in range(r + 1, self._m):
                multiples_of_row_r = self.augmented_matrix[r_below][c]
                if not is_zero(multiples_of_row_r):
                    self.augmented_matrix[r_below] = self.augmented_matrix[r_below] \
                                                     - multiples_of_row_r * self.augmented_matrix[r]
            self.pivots.append(c)
            r += 1
            c += 1

    def _backward(self) -> None:
        """
        后向过程 (从下到上)

        对从下到上 (从行最简形式 matrix 倒数第一个非零行开始, 到第二行结束) 每一行执行以下操作:
            主元上面的所有行减去主元所在行的某个倍数, 使得主元 (第 r 行, 第 c 列) 上面所有元素都为 0
        """
        # r = 2
        # c = 4
        # row -2:
        # [ 1 -1 2 0  3 | 1 ]    [ 1 -1 2 0 0 | -5 ]
        # [ 0  0 1 1 -1 | 3 ] => [ 0  0 1 1 0 |  5 ]
        # [ 0  0 0 0  1 | 2 ]    [ 0  0 0 0 1 |  2 ]
        # [ 0  0 0 0  0 | 0 ]    [ 0  0 0 0 0 |  0 ]
        #
        # r = 1
        # c = 2
        # row -3:
        # [ 1 -1 2 0 0 | -5 ]    [ 1 -1 0 -2 0 | -15 ]
        # [ 0  0 1 1 0 |  5 ] => [ 0  0 1  1 0 |  5  ]
        # [ 0  0 0 0 1 |  2 ]    [ 0  0 0  0 1 |  2  ]
        # [ 0  0 0 0 0 |  0 ]    [ 0  0 0  0 0 |  0  ]

        # loop rows
        for r in range(len(self.pivots) - 1, 0, -1):
            c = self.pivots[r]
            for r_above in range(r - 1, -1, -1):
                multiples_of_row_r = self.augmented_matrix[r_above][c]
                if not is_zero(multiples_of_row_r):
                    self.augmented_matrix[r_above] = self.augmented_matrix[r_above] \
                                                     - multiples_of_row_r * self.augmented_matrix[r]

    def _max_row_below(self, r: int, c: int) -> int:
        """返回当前行的下面所有行中具有最大主元的行"""
        # 初始化具有最大主元的行为当前行, 最大主元为当前行的主元
        max_row = r
        max_value = abs(self.augmented_matrix[r][c])
        # 遍历 r 行的下面所有行
        for i in range(r + 1, self._m):
            if abs(self.augmented_matrix[i][c]) > max_value:
                max_row = i
                max_value = self.augmented_matrix[i][c]
        return max_row

    def _swap_row(self, r1: int, r2: int) -> None:
        """交换当前增广矩阵中的两行"""
        self.augmented_matrix[r1], self.augmented_matrix[r2] = self.augmented_matrix[r2], self.augmented_matrix[r1]

    def augmented_matrix_fancy_print(self) -> None:
        """打印当前增广矩阵"""
        for r in range(self._m):
            print(" ".join(str(self.augmented_matrix[r][c]) for c in range(self._n)), end=" ")
            print("|", self.augmented_matrix[r][-1])

    def determine_solution(self) -> str:
        """判断当前线性系统对应的增广矩阵的解的情况"""

        # 行最简形式 matrix 非零行
        matrix_not_zero_count = len(self.pivots)
        # 行最简形式 augmented_matrix 非零行
        augmented_matrix_not_zero_count = matrix_not_zero_count
        for zero_r in range(len(self.pivots), self._m):
            if not is_zero(self.augmented_matrix[zero_r][-1]):
                augmented_matrix_not_zero_count += 1
        # 未知数个数
        x_count = self._n

        # R2-a: 行最简形式 matrix 非零行 < 行最简形式 augmented_matrix 非零行: 无解
        # R2-b: 行最简形式 matrix 非零行 < 未知数个数: 无数解
        # R2-c: 行最简形式 matrix 非零行 = 未知数个数: 唯一解
        if matrix_not_zero_count < augmented_matrix_not_zero_count:
            return "NO"
        if matrix_not_zero_count < x_count:
            return "MULTIPLE"
        if matrix_not_zero_count == x_count:
            return "ONE"
        return "ERROR"
