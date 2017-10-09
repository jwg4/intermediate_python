from math import floor, sqrt


def root_convergents(n):
    l = []
    for a in cf_expansion(n):
        l.append(a)
        yield evaluate_cf(l)


def cf_expansion(n):
    m = 0
    d = 1
    a = a0 = int(floor(sqrt(n)))
    while True:
        yield a
        m = d * a - m
        d = (n - m * m) / d
        a = (a0 + m) / d


def evaluate_cf(l):
    a, b = (1, 0)
    for j in l[::-1]:
        a, b = (j * a + b, a)
    return a, b


def pell_approximation(n, a, b):
    return a**2 - 7 * b**2


def fundamental_solution(n):
    for a, b in root_convergents(n):
        if pell_approximation(n, a, b) == 1:
            return a, b
