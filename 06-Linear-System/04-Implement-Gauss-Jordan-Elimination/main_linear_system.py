from la.linear_system import LinearSystem
from la.matrix import Matrix
from la.vector import Vector

if __name__ == "__main__":
    # 1.0 0.0 0.0 | 2.0
    # -0.0 1.0 0.0 | -1.5
    # 0.0 0.0 1.0 | 1.0
    matrix = Matrix([[0, 4, 8], [2, 2, 1], [4, 8, 8]])
    vector = Vector([2, 2, 4])
    linear_system = LinearSystem(matrix, vector)
    linear_system.gauss_jordan_elimination()
    linear_system.augmented_matrix_fancy_print()

    print("------")

    # 1.0 0.0 0.0 | -1.0
    # 0.0 1.0 0.0 | -2.0
    # -0.0 -0.0 1.0 | 3.0
    matrix = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    vector = Vector([7, -11, 1])
    linear_system = LinearSystem(matrix, vector)
    linear_system.gauss_jordan_elimination()
    linear_system.augmented_matrix_fancy_print()

    print("------")

    # 1.0 0.0 0.0 | 2.0
    # 0.0 1.0 0.0 | -3.0
    # 0.0 0.0 1.0 | -4.0
    matrix = Matrix([[1, -3, 5], [2, -1, -3], [3, 1, 4]])
    vector = Vector([-9, 19, -13])
    linear_system = LinearSystem(matrix, vector)
    linear_system.gauss_jordan_elimination()
    linear_system.augmented_matrix_fancy_print()

    print("------")

    # 1.0 0.0 0.0 | 1.0
    # -0.0 1.0 0.0 | 1.0
    # 0.0 0.0 1.0 | 1.0
    matrix = Matrix([[1, 1, 1], [1, -1, -1], [2, 1, 5]])
    vector = Vector([3, -1, 8])
    linear_system = LinearSystem(matrix, vector)
    linear_system.gauss_jordan_elimination()
    linear_system.augmented_matrix_fancy_print()

    print("------")

    # 1.0 0.0 0.0 | 3.0
    # 0.0 1.0 0.0 | 1.0
    # 0.0 0.0 1.0 | -2.0
    matrix = Matrix([[1, 3, 2], [2, 7, 7], [2, 5, 2]])
    vector = Vector([2, -1, 7])
    linear_system = LinearSystem(matrix, vector)
    linear_system.gauss_jordan_elimination()
    linear_system.augmented_matrix_fancy_print()

    print("------")

    # 1.0 0.0 0.0 | 2.9999999999999996
    # 0.0 1.0 0.0 | -2.999999999999999
    # -0.0 -0.0 1.0 | 2.0
    matrix = Matrix([[6, -3, 2], [5, 1, 12], [8, 5, 1]])
    vector = Vector([31, 36, 11])
    linear_system = LinearSystem(matrix, vector)
    linear_system.gauss_jordan_elimination()
    linear_system.augmented_matrix_fancy_print()

    print("------")

    # 1.0 0.0 3.7007434154171876e-17 | 3.0
    # 0.0 1.0 -4.440892098500626e-16 | -4.000000000000001
    # 0.0 0.0 0.9999999999999999 | 0.5000000000000001
    matrix = Matrix([[3, 1, -2], [5, -3, 10], [7, 4, 16]])
    vector = Vector([4, 32, 13])
    linear_system = LinearSystem(matrix, vector)
    linear_system.gauss_jordan_elimination()
    linear_system.augmented_matrix_fancy_print()
