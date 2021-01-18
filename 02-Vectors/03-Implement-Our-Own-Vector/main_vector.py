from la.vector import Vector

if __name__ == "__main__":
    # vector = [5, 2]
    # vector2 = [3, 1]
    vector = Vector([5, 2])
    vector2 = Vector([3, 1])
    print("vector = {}".format(vector))
    print("vector2 = {}".format(vector2))

    print("------")

    # len(vector) = 2
    # vector[0] = 5, vector[1] = 2
    print("len(vector) = {}".format(len(vector)))
    print("vector[0] = {}, vector[1] = {}".format(vector[0], vector[1]))
