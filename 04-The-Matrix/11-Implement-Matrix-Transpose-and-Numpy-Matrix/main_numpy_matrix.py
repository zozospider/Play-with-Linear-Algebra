import numpy as np

if __name__ == "__main__":
    print(np.__version__)

    # 创建
    A = np.array([[1, 2], [3, 4]])
    # [[1 2]
    #  [3 4]]
    print(A)
    B = np.array([[10, 20], [30, 40]])
    # [[10 20]
    #  [30 40]]
    print(B)
    v = np.array([1, 10])
    # [ 1 10]
    print(v)

    # 形状
    # (2, 2)
    print(A.shape)

    # 转置
    # [[1 3]
    #  [2 4]]
    print(A.T)

    # 元素
    # 4
    print(A[1, 1])

    # 行向量
    # [1 2]
    print(A[0])
    # [1 2]
    print(A[0, :])

    # 列向量
    # [1 3]
    print(A[:, 0])

    # 运算
    # [[11 22]
    #  [33 44]]
    print(A + B)
    # [[2 3]
    #  [4 5]]
    print(A + 1)
    # [[ -9 -18]
    #  [-27 -36]]
    print(A - B)
    # [[0 1]
    #  [2 3]]
    print(A - 1)
    # [[10 20]
    #  [30 40]]
    print(A * 10)
    # [[10 20]
    #  [30 40]]
    print(10 * A)
    # [[ 10  40]
    #  [ 90 160]]
    print(A * B)
    # [[ 70 100]
    #  [150 220]]
    print(A.dot(B))

    # [[ 2 12]
    #  [ 4 14]]
    print(A + v)
    # [[ 0 -8]
    #  [ 2 -6]]
    print(A - v)
    # [21 43]
    print(A.dot(v))
