def count_to_infinity(start=1):
    i = start
    while True:
        yield i
        i = i + 1


def all_the_squares():
    for n in count_to_infinity(0):
        yield n * n


if __name__ == '__main__':
    numbers = all_the_squares()
    for n, c in zip(numbers, ["a", "b", "c", "d", "e"]):
        print(n, c)
