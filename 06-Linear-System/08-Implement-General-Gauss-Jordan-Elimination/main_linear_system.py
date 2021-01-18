from la.linear_system import LinearSystem
from la.matrix import Matrix
from la.vector import Vector

if __name__ == "__main__":
    # 1.0 0.0 0.0 | 2.0
    # -0.0 1.0 0.0 | -1.5
    # 0.0 0.0 1.0 | 1.0
    # ONE
    # [0, 1, 2]
    matrix = Matrix([[0, 4, 8], [2, 2, 1], [4, 8, 8]])
    vector = Vector([2, 2, 4])
    linear_system = LinearSystem(matrix, vector)
    linear_system.gauss_jordan_elimination()
    linear_system.augmented_matrix_fancy_print()
    print(linear_system.determine_solution())
    print(linear_system.pivots)

    print("------")

    # 1.0 0.0 0.0 | -1.0
    # 0.0 1.0 0.0 | -2.0
    # -0.0 -0.0 1.0 | 3.0
    # ONE
    # [0, 1, 2]
    matrix = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    vector = Vector([7, -11, 1])
    linear_system = LinearSystem(matrix, vector)
    linear_system.gauss_jordan_elimination()
    linear_system.augmented_matrix_fancy_print()
    print(linear_system.determine_solution())
    print(linear_system.pivots)

    print("------")

    # 1.0 0.0 3.7007434154171876e-17 | 3.0
    # 0.0 1.0 -4.440892098500626e-16 | -4.000000000000001
    # 0.0 0.0 0.9999999999999999 | 0.5000000000000001
    # ONE
    # [0, 1, 2]
    matrix = Matrix([[3, 1, -2], [5, -3, 10], [7, 4, 16]])
    vector = Vector([4, 32, 13])
    linear_system = LinearSystem(matrix, vector)
    linear_system.gauss_jordan_elimination()
    linear_system.augmented_matrix_fancy_print()
    print(linear_system.determine_solution())
    print(linear_system.pivots)

    print("------")

    # 1.0 -1.0 0.0 -2.0 0.0 | -15.0
    # 0.0 0.0 1.0 1.0 0.0 | 5.0
    # 0.0 0.0 0.0 0.0 1.0 | 2.0
    # 0.0 0.0 0.0 0.0 0.0 | 0.0
    # MULTIPLE
    # [0, 2, 4]
    matrix = Matrix([[1, -1, 2, 0, 3], [-1, 1, 0, 2, -5], [1, -1, 4, 2, 4], [-2, 2, -5, -1, -3]])
    vector = Vector([1, 5, 13, -1])
    linear_system = LinearSystem(matrix, vector)
    linear_system.gauss_jordan_elimination()
    linear_system.augmented_matrix_fancy_print()
    print(linear_system.determine_solution())
    print(linear_system.pivots)

    print("------")

    # 1.0 -1.0 0.0 0.0 0.0 | -5.0
    # 0.0 0.0 1.0 0.0 0.0 | 0.0
    # 0.0 0.0 0.0 1.0 0.0 | 5.0
    # 0.0 0.0 0.0 0.0 1.0 | 2.0
    # MULTIPLE
    # [0, 2, 3, 4]
    matrix = Matrix([[1, -1, 2, 0, 3], [-1, 1, 0, 2, -5], [1, -1, 4, 2, 4], [-2, 2, 5, -1, -3]])
    vector = Vector([1, 5, 13, -1])
    linear_system = LinearSystem(matrix, vector)
    linear_system.gauss_jordan_elimination()
    linear_system.augmented_matrix_fancy_print()
    print(linear_system.determine_solution())
    print(linear_system.pivots)

    print("------")

    # 1.0 0.0 | 0.0
    # -0.0 1.0 | -0.0
    # 0.0 0.0 | 0.0
    # 0.0 0.0 | 0.0
    # 0.0 0.0 | 0.0
    # ONE
    # [0, 1]
    matrix = Matrix([[2, 1], [4, 2], [8, 4], [16, 8], [32, 8]])
    vector = Vector([0, 0, 0, 0, 0])
    linear_system = LinearSystem(matrix, vector)
    linear_system.gauss_jordan_elimination()
    linear_system.augmented_matrix_fancy_print()
    print(linear_system.determine_solution())
    print(linear_system.pivots)

    print("------")

    # 1.0 0.0 | 1.0
    # -0.0 1.0 | 0.5
    # 0.0 0.0 | 5.0
    # NO
    # [0, 1]
    matrix = Matrix([[2, 2], [2, 1], [1, 2]])
    vector = Vector([3, 2.5, 7])
    linear_system = LinearSystem(matrix, vector)
    linear_system.gauss_jordan_elimination()
    linear_system.augmented_matrix_fancy_print()
    print(linear_system.determine_solution())
    print(linear_system.pivots)
