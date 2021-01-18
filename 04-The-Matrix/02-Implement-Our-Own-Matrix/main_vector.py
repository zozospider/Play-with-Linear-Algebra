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
    # [5, 2] / 2 = [2.5, 1.0]
    # +[5, 2] = [5, 2]
    # -[5, 2] = [-5, -2]
    print("{} + {} = {}".format(vector, vector2, vector + vector2))
    print("{} + {} = {}".format(vector, zero_2, vector + zero_2))
    print("{} - {} = {}".format(vector, vector2, vector - vector2))
    print("{} - {} = {}".format(vector, zero_2, vector - zero_2))
    print("{} * {} = {}".format(vector, 3, vector * 3))
    print("{} * {} = {}".format(3, vector, 3 * vector))
    print("{} / {} = {}".format(vector, 2, vector / 2))
    print("+{} = {}".format(vector, +vector))
    print("-{} = {}".format(vector, -vector))

    print("------")

    # [5, 2].norm() = 5.385164807134504
    # [3, 1].norm() = 3.1622776601683795
    # [0, 0].norm() = 0.0
    print("{}.norm() = {}".format(vector, vector.norm()))
    print("{}.norm() = {}".format(vector2, vector2.norm()))
    print("{}.norm() = {}".format(zero_2, zero_2.norm()))

    # [5, 2].normalize() = [0.9284766908852593, 0.3713906763541037]
    # [3, 1].normalize() = [0.9486832980505138, 0.31622776601683794]
    # Cannot normalize zero vector [0, 0]
    print("{}.normalize() = {}".format(vector, vector.normalize()))
    print("{}.normalize() = {}".format(vector2, vector2.normalize()))
    try:
        print("{}.normalize() = {}".format(zero_2, zero_2.normalize()))
    except ZeroDivisionError:
        print("Cannot normalize zero vector {}".format(zero_2))

    # [5, 2].normalize().norm() = 1.0
    # [3, 1].normalize().norm() = 0.9999999999999999
    print("{}.normalize().norm() = {}".format(vector, vector.normalize().norm()))
    print("{}.normalize().norm() = {}".format(vector2, vector2.normalize().norm()))

    print("------")

    # [5, 2].dot([3, 1]) = 17
    print("{}.dot({}) = {}".format(vector, vector2, vector.dot(vector2)))
