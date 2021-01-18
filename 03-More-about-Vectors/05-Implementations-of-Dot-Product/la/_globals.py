EPSILON = 1e-8


def is_zero(number: float) -> bool:
    return abs(number) < EPSILON


def is_equal(a: float, b: float) -> bool:
    return abs(a - b) < EPSILON
