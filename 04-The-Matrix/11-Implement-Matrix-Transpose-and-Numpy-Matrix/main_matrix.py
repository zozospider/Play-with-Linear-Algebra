from playLA.matrix import Matrix
from playLA.vector import Vector

if __name__ == "__main__":
    # matrix: [[1, 2], [3, 4]]
    # matrix2: [[10, 20], [30, 40]]
    # matrix3: [[1, 2, 0], [2, 1, 5], [1, 1, 2], [1, 0, 0], [4, 1, 2]]
    # matrix4: [[2, 0], [1, 3], [0, 1]]
    # zero_2_2: [[0, 0], [0, 0]]
    # zero_2_3: [[0, 0, 0], [0, 0, 0]]
    # vector: [2, 1, 0]
    matrix = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[10, 20], [30, 40]])
    matrix3 = Matrix([[1, 2, 0], [2, 1, 5], [1, 1, 2], [1, 0, 0], [4, 1, 2]])
    matrix4 = Matrix([[2, 0], [1, 3], [0, 1]])
    zero_2_2 = Matrix.zero(2, 2)
    zero_2_3 = Matrix.zero(2, 3)
    vector = Vector([2, 1, 0])
    print("matrix:", matrix)
    print("matrix2:", matrix2)
    print("matrix3:", matrix3)
    print("matrix4:", matrix4)
    print("zero_2_2:", zero_2_2)
    print("zero_2_3:", zero_2_3)
    print("vector:", vector)

    print("------")

    # matrix[0]: [1, 2]
    # matrix[0, 1]: 2
    # matrix.shape(): (2, 2)
    # matrix.row_num(): 2
    # len(matrix): 2
    # matrix.col_num(): 2
    # matrix.size(): 4
    # matrix.row_vector(0): [1, 2]
    # matrix.col_vector(0): [1, 3]
    print("matrix[0]:", matrix[0])
    print("matrix[0, 1]:", matrix[0][1])
    print("matrix.shape():", matrix.shape())
    print("matrix.row_num():", matrix.row_num())
    print("len(matrix):", len(matrix))
    print("matrix.col_num():", matrix.col_num())
    print("matrix.size():", matrix.size())
    print("matrix.row_vector(0):", matrix.row_vector(0))
    print("matrix.col_vector(0):", matrix.col_vector(0))

    print("------")

    # [[1, 2], [3, 4]] + [[10, 20], [30, 40]] = [[11, 22], [33, 44]]
    # [[1, 2], [3, 4]] + [[0, 0], [0, 0]] = [[1, 2], [3, 4]]
    # [[1, 2], [3, 4]] - [[10, 20], [30, 40]] = [[-9, -18], [-27, -36]]
    # [[1, 2], [3, 4]] - [[0, 0], [0, 0]] = [[1, 2], [3, 4]]
    # [[1, 2], [3, 4]] * 2 = [[2, 4], [6, 8]]
    # 2 * [[1, 2], [3, 4]] = [[2, 4], [6, 8]]
    # [[1, 2], [3, 4]] / 2 = [[0.5, 1.0], [1.5, 2.0]]
    # +[[1, 2], [3, 4]] = [[1, 2], [3, 4]]
    # -[[1, 2], [3, 4]] = [[-1, -2], [-3, -4]]
    print("{} + {} = {}".format(matrix, matrix2, matrix + matrix2))
    print("{} + {} = {}".format(matrix, zero_2_2, matrix + zero_2_2))
    print("{} - {} = {}".format(matrix, matrix2, matrix - matrix2))
    print("{} - {} = {}".format(matrix, zero_2_2, matrix - zero_2_2))
    print("{} * {} = {}".format(matrix, 2, matrix * 2))
    print("{} * {} = {}".format(2, matrix, 2 * matrix))
    print("{} / {} = {}".format(matrix, 2, matrix / 2))
    print("+{} = {}".format(matrix, +matrix))
    print("-{} = {}".format(matrix, -matrix))

    print("------")

    # [[1, 2, 0], [2, 1, 5], [1, 1, 2], [1, 0, 0], [4, 1, 2]].dot([2, 1, 0])
    #                                                           = [4, 5, 3, 2, 9]
    print("{}.dot({}) = {}".format(matrix3, vector, matrix3.dot(vector)))
    # print("{}.dot({}) = {}".format(matrix4, vector, matrix4.dot(vector)))

    # [[1, 2, 0], [2, 1, 5], [1, 1, 2], [1, 0, 0], [4, 1, 2]].dot([[2, 0], [1, 3], [0, 1]])
    #                                                           = [[4, 6], [5, 8], [3, 5], [2, 0], [9, 5]]
    print("{}.dot({}) = {}".format(matrix3, matrix4, matrix3.dot(matrix4)))
    # print("{}.dot({}) = {}".format(matrix4, matrix3, matrix4.dot(matrix3)))

    print("------")

    # [[2, 0], [1, 3], [0, 1]].transpose() = [[2, 1, 0], [0, 3, 1]]
    print("{}.transpose() = {}".format(matrix4, matrix4.transpose()))
