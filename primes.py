def calculate_primes_less_than(n):
    l = [2]
    for i in range(3, n):
        if all((i % p != 0) for p in l):
            l.append(i)

    return l


def calculate_primes_between(a, b, primes):
    pass
    
