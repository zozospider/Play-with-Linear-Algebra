from playLA.vector import Vector

if __name__ == "__main__":
    # vec = [5, 2]
    # vec2 = [3, 1]
    vec = Vector([5, 2])
    vec2 = Vector([3, 1])
    print("vec = {}".format(vec))
    print("vec2 = {}".format(vec2))

    print("------")

    # len(vec) = 2
    # vec[0] = 5, vec[1] = 2
    print("len(vec) = {}".format(len(vec)))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))
