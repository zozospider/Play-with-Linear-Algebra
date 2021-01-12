from playLA.Matrix import Matrix

if __name__ == "__main__":
    # matrix: Matrix([[1, 2], [3, 4]])
    # matrix[0, 0]: 1
    # matrix.shape(): (2, 2)
    # matrix.row_num(): 2
    # len(matrix): 2
    # matrix.col_num(): 2
    # matrix.size(): 4
    # matrix.row_vector(0): (1, 2)
    # matrix.col_vector(0): (1, 3)
    matrix = Matrix([[1, 2], [3, 4]])
    print("matrix:", matrix)
    print("matrix[0, 0]:", matrix[0, 0])
    print("matrix.shape():", matrix.shape())
    print("matrix.row_num():", matrix.row_num())
    print("len(matrix):", len(matrix))
    print("matrix.col_num():", matrix.col_num())
    print("matrix.size():", matrix.size())
    print("matrix.row_vector(0):", matrix.row_vector(0))
    print("matrix.col_vector(0):", matrix.col_vector(0))
