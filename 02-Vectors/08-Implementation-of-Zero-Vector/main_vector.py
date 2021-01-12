from playLA.Vector import Vector

if __name__ == "__main__":
    vec = Vector([5, 2])
    vec2 = Vector([3, 1])
    zero2 = Vector.zero(2)

    # vec = (5, 2)
    # zero2 = (0, 0)
    # len(vec) = 2
    # vec[0] = 5, vec[1] = 2
    print("vec = {}".format(vec))
    print("zero2 = {}".format(zero2))
    print("len(vec) = {}".format(len(vec)))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))

    # (5, 2) + (3, 1) = (8, 3)
    # (5, 2) + (0, 0) = (5, 2)
    # (5, 2) - (3, 1) = (2, 1)
    # (5, 2) * 3 = (15, 6)
    # 3 * (5, 2) = (15, 6)
    # +(5, 2) = (5, 2)
    # -(5, 2) = (-5, -2)
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} + {} = {}".format(vec, zero2, vec + zero2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))
    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))
