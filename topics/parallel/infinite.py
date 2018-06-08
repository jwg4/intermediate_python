def count_to_infinity(start=1):
    i = start
    while True:
        yield i
        i = i + 1


if __name__ == '__main__':
    numbers = count_to_infinity(0)
    for n, c in zip(numbers, ["a", "b", "c", "d", "e"]):
        print(n, c)