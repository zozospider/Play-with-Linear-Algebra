import numpy as np

if __name__ == "__main__":
    print(np.__version__)

    # lst: [0, 1, 9]
    lst = [0, 1, 2]
    lst[2] = "a"
    lst[2] = 9
    print("lst:", lst)

    # vec: [0 1 9]
    vec = np.array([0, 1, 2])
    # vec[2] = "a"
    vec[2] = 9
    print("vec:", vec)

    print("------")

    # np array 的创建
    # np.zeros(5): [0. 0. 0. 0. 0.]
    # np.ones(5): [1. 1. 1. 1. 1.]
    # np.full(5, 9): [9 9 9 9 9]
    print("np.zeros(5):", np.zeros(5))
    print("np.ones(5):", np.ones(5))
    print("np.full(5, 9):", np.full(5, 9))

    print("------")

    # np array 的基本属性
    # vec: [0 1 2]
    # vec.size: 3
    # len(vec): 3
    # vec[0]: 0
    # vec[-1]: 2
    # vec[0:2]: [0 1]
    # type(vec[0:2]): <class 'numpy.ndarray'>
    vec = np.array([0, 1, 2])
    print("vec:", vec)
    print("vec.size:", vec.size)
    print("len(vec):", len(vec))
    print("vec[0]:", vec[0])
    print("vec[-1]:", vec[-1])
    print("vec[0:2]:", vec[0:2])
    print("type(vec[0:2]):", type(vec[0:2]))

    print("------")

    # np array 的基本运算
    vec1 = np.array([1, 2, 3])
    vec2 = np.array([10, 20, 30])

    # [1 2 3] + [10 20 30] = [11 22 33]
    # [1 2 3] - [10 20 30] = [-9 - 18 - 27]
    # 2 * [1 2 3] = [2 4 6]
    # [1 2 3] * 2 = [2 4 6]
    # [1 2 3] * [10 20 30] = [10 40 90]
    print("{} + {} = {}".format(vec1, vec2, vec1 + vec2))
    print("{} - {} = {}".format(vec1, vec2, vec1 - vec2))
    print("{} * {} = {}".format(2, vec1, 2 * vec1))
    print("{} * {} = {}".format(vec1, 2, vec1 * 2))
    print("{} * {} = {}".format(vec1, vec2, vec1 * vec2))

    # [1 2 3].dot([10 20 30]) = 140
    # np.linalg.norm(vec1): 3.7416573867739413
    # vec1 / np.linalg.norm(vec1): [0.26726124 0.53452248 0.80178373]
    # np.linalg.norm(vec / np.linalg.norm(vec)): 0.9999999999999999
    print("{}.dot({}) = {}".format(vec1, vec2, vec1.dot(vec2)))
    print("np.linalg.norm(vec1):", np.linalg.norm(vec1))
    print("vec1 / np.linalg.norm(vec1):", vec1 / np.linalg.norm(vec1))
    print("np.linalg.norm(vec / np.linalg.norm(vec)):", np.linalg.norm(vec / np.linalg.norm(vec)))
    # zero3 = np.zeros(3)
    # print(zero3 / np.linalg.norm(zero3))
