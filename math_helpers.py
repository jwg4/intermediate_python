def eea(a, b):
    x, y = a, b
    m, n = 1, 0
    o, p = 0, 1

    while y:
        q = x / y
        
        x, y = y, x - q * y
        m, o = o, m - q * o 
        n, p = p, n - q * p

    return x, m, n 
