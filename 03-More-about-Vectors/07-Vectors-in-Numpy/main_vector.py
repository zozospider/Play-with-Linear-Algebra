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

    print("------")

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

    print("------")

    # norm((5, 2)) = 5.385164807134504
    # norm((3, 1)) = 3.1622776601683795
    # norm((0, 0)) = 0.0
    print("norm({}) = {}".format(vec, vec.norm()))
    print("norm({}) = {}".format(vec2, vec2.norm()))
    print("norm({}) = {}".format(zero2, zero2.norm()))

    # normalize(5, 2) is (0.9284766908852593, 0.3713906763541037)
    # normalize(3, 1) is (0.9486832980505138, 0.31622776601683794)
    # Cannot normalize zero vector (0, 0)
    print("normalize {} is {}".format(vec, vec.normalize()))
    print("normalize {} is {}".format(vec2, vec2.normalize()))
    try:
        print("normalize {} is {}".format(zero2, zero2.normalize()))
    except ZeroDivisionError:
        print("Cannot normalize zero vector {}".format(zero2))

    # 0.9999999999999999
    # 1.0
    print(vec2.normalize().norm())
    print(vec.normalize().norm())

    print("------")

    # (5, 2).dot((3, 1)) = 17
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2)))
