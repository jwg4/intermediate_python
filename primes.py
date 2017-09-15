from math import sqrt


def calculate_primes_less_than(n):
    l = [2]
    for i in range(3, n):
        if all((i % p != 0) for p in l):
            l.append(i)

    return l


def generate_primes_between(a, b, primes):
    for i in range(a, b+1):
        if all(
            all((i % p != 0) for p in l)
            for l in primes
            ):
            yield i


def calculate_primes_between(a, b, primes):
    return list(generate_primes_between(a, b, primes))
    

def can_test_to(n):
    return (n + 1)**2 - 1
    

def need_to_test(n):
    return int(sqrt(n))
