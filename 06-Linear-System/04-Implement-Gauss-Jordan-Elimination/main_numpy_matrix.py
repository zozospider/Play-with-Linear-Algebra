import numpy as np

if __name__ == "__main__":
    print(np.__version__)

    # 创建
    # [[1 2]
    #  [3 4]]
    matrix1 = np.array([[1, 2], [3, 4]])
    print(matrix1)

    # [[10 20]
    #  [30 40]]
    matrix2 = np.array([[10, 20], [30, 40]])
    print(matrix2)

    # [[2 0 1]
    #  [1 2 2]
    #  [0 2 2]]
    matrix3 = np.array([[2, 0, 1], [1, 2, 2], [0, 2, 2]])
    print(matrix3)

    # [ 1 10]
    vector = np.array([1, 10])
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

    print("------")

    # 单位矩阵
    # [[1. 0. 0.]
    #  [0. 1. 0.]
    #  [0. 0. 1.]]
    identity_3 = np.identity(3)
    print(identity_3)

    # [[2. 0. 1.]
    #  [1. 2. 2.]
    #  [0. 2. 2.]]
    print(matrix3.dot(identity_3))
    # [[2. 0. 1.]
    #  [1. 2. 2.]
    #  [0. 2. 2.]]
    print(identity_3.dot(matrix3))

    print("------")

    # 逆矩阵
    # [[ 0.   1.  -1. ]
    #  [-1.   2.  -1.5]
    #  [ 1.  -2.   2. ]]
    inverted_matrix3 = np.linalg.inv(matrix3)
    print(inverted_matrix3)

    # [[1. 0. 0.]
    #  [0. 1. 0.]
    #  [0. 0. 1.]]
    print(inverted_matrix3.dot(matrix3))
    # [[1. 0. 0.]
    #  [0. 1. 0.]
    #  [0. 0. 1.]]
    print(matrix3.dot(inverted_matrix3))
