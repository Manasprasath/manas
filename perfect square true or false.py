import math


def is_perfect_square(number: int) -> bool:
    """
    Returns True if the provided number is a
    perfect square (and False otherwise).
    """
    return math.isqrt(number) ** 2 == number


# Some random integer values
values = [
    3, 25, 81, 100, 1750,
    4539, 5776, 15623,
]

# See if each value is a perfect square
for value in values:
    print("Is", value, "a perfect square?", is_perfect_square(value))
