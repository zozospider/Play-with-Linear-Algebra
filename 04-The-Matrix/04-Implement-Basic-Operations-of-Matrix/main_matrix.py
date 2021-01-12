from playLA.Matrix import Matrix

if __name__ == "__main__":
    # matrix: [[1, 2], [3, 4]]
    # matrix2: [[10, 20], [30, 40]]
    matrix = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[10, 20], [30, 40]])
    print("matrix:", matrix)
    print("matrix2:", matrix2)

    print("------")

    # matrix[0, 0]: 1
    # matrix.shape(): (2, 2)
    # matrix.row_num(): 2
    # len(matrix): 2
    # matrix.col_num(): 2
    # matrix.size(): 4
    # matrix.row_vector(0): [1, 2]
    # matrix.col_vector(0): [1, 3]
    print("matrix[0, 0]:", matrix[0, 0])
    print("matrix.shape():", matrix.shape())
    print("matrix.row_num():", matrix.row_num())
    print("len(matrix):", len(matrix))
    print("matrix.col_num():", matrix.col_num())
    print("matrix.size():", matrix.size())
    print("matrix.row_vector(0):", matrix.row_vector(0))
    print("matrix.col_vector(0):", matrix.col_vector(0))

    print("------")

    # [[1, 2], [3, 4]].add([[10, 20], [30, 40]]): [[11, 22], [33, 44]]
    print("{}.add({}): {}".format(matrix, matrix2, matrix.add(matrix2)))
