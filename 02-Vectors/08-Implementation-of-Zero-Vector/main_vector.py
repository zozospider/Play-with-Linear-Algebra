from la.vector import Vector

if __name__ == "__main__":
    # vector = [5, 2]
    # vector2 = [3, 1]
    # zero_2 = [0, 0]
    # zero_3 = [0, 0, 0]
    vector = Vector([5, 2])
    vector2 = Vector([3, 1])
    zero_2 = Vector.zero(2)
    zero_3 = Vector.zero(3)
    print("vector = {}".format(vector))
    print("vector2 = {}".format(vector2))
    print("zero_2 = {}".format(zero_2))
    print("zero_3 = {}".format(zero_3))

    print("------")

    # len(vector) = 2
    # vector[0] = 5, vector[1] = 2
    print("len(vector) = {}".format(len(vector)))
    print("vector[0] = {}, vector[1] = {}".format(vector[0], vector[1]))

    print("------")

    # [5, 2] + [3, 1] = [8, 3]
    # [5, 2] + [0, 0] = [5, 2]
    # [5, 2] - [3, 1] = [2, 1]
    # [5, 2] - [0, 0] = [5, 2]
    # [5, 2] * 3 = [15, 6]
    # 3 * [5, 2] = [15, 6]
    # +[5, 2] = [5, 2]
    # -[5, 2] = [-5, -2]
    print("{} + {} = {}".format(vector, vector2, vector + vector2))
    print("{} + {} = {}".format(vector, zero_2, vector + zero_2))
    print("{} - {} = {}".format(vector, vector2, vector - vector2))
    print("{} - {} = {}".format(vector, zero_2, vector - zero_2))
    print("{} * {} = {}".format(vector, 3, vector * 3))
    print("{} * {} = {}".format(3, vector, 3 * vector))
    print("+{} = {}".format(vector, +vector))
    print("-{} = {}".format(vector, -vector))
