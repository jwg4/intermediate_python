import random


def count_to_infinity(start=1):
    i = start
    while True:
        yield i
        i = i + 1


def all_the_squares():
    for n in count_to_infinity(0):
        yield n * n


def some_natural_numbers(p=0.1):
    for n in count_to_infinity():
        yield n
        if random.uniform(0, 1) < p:
            return


if __name__ == '__main__':
    numbers = all_the_squares()
    for n, c in zip(numbers, ["a", "b", "c", "d", "e"]):
        print(n, c)
