from math import floor, sqrt


def root_convergents(n):
    a = floor(sqrt(n))
    b = 1
    while True:
        yield (a, b)
