import numpy as np

if __name__ == "__main__":
    print(np.__version__)

    # 创建
    matrix1 = np.array([[1, 2], [3, 4]])
    # [[1 2]
    #  [3 4]]
    print(matrix1)
    matrix2 = np.array([[10, 20], [30, 40]])
    # [[10 20]
    #  [30 40]]
    print(matrix2)
    vector = np.array([1, 10])
    # [ 1 10]
    print(vector)

    # 形状
    # (2, 2)
    print(matrix1.shape)

    # 转置
    # [[1 3]
    #  [2 4]]
    print(matrix1.T)

    # 元素
    # 4
    print(matrix1[1, 1])

    # 行向量
    # [1 2]
    print(matrix1[0])
    # [1 2]
    print(matrix1[0, :])

    # 列向量
    # [1 3]
    print(matrix1[:, 0])

    # 运算
    # [[11 22]
    #  [33 44]]
    print(matrix1 + matrix2)
    # [[2 3]
    #  [4 5]]
    print(matrix1 + 1)
    # [[ -9 -18]
    #  [-27 -36]]
    print(matrix1 - matrix2)
    # [[0 1]
    #  [2 3]]
    print(matrix1 - 1)
    # [[10 20]
    #  [30 40]]
    print(matrix1 * 10)
    # [[10 20]
    #  [30 40]]
    print(10 * matrix1)
    # [[ 10  40]
    #  [ 90 160]]
    print(matrix1 * matrix2)
    # [[ 70 100]
    #  [150 220]]
    print(matrix1.dot(matrix2))

    # [[ 2 12]
    #  [ 4 14]]
    print(matrix1 + vector)
    # [[ 0 -8]
    #  [ 2 -6]]
    print(matrix1 - vector)
    # [21 43]
    print(matrix1.dot(vector))
