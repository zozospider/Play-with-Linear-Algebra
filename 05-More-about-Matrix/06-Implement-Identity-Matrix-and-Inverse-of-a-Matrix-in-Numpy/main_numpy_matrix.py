import numpy as np

if __name__ == "__main__":
    print(np.__version__)

    # 创建
    M1 = np.array([[1, 2], [3, 4]])
    # [[1 2]
    #  [3 4]]
    print(M1)
    M2 = np.array([[10, 20], [30, 40]])
    # [[10 20]
    #  [30 40]]
    print(M2)
    V = np.array([1, 10])
    # [ 1 10]
    print(V)

    # 形状
    # (2, 2)
    print(M1.shape)

    # 转置
    # [[1 3]
    #  [2 4]]
    print(M1.T)

    # 元素
    # 4
    print(M1[1, 1])

    # 行向量
    # [1 2]
    print(M1[0])
    # [1 2]
    print(M1[0, :])

    # 列向量
    # [1 3]
    print(M1[:, 0])

    # 运算
    # [[11 22]
    #  [33 44]]
    print(M1 + M2)
    # [[2 3]
    #  [4 5]]
    print(M1 + 1)
    # [[ -9 -18]
    #  [-27 -36]]
    print(M1 - M2)
    # [[0 1]
    #  [2 3]]
    print(M1 - 1)
    # [[10 20]
    #  [30 40]]
    print(M1 * 10)
    # [[10 20]
    #  [30 40]]
    print(10 * M1)
    # [[ 10  40]
    #  [ 90 160]]
    print(M1 * M2)
    # [[ 70 100]
    #  [150 220]]
    print(M1.dot(M2))

    # [[ 2 12]
    #  [ 4 14]]
    print(M1 + V)
    # [[ 0 -8]
    #  [ 2 -6]]
    print(M1 - V)
    # [21 43]
    print(M1.dot(V))
