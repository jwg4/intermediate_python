def partitions_below(n, m):
    if n == 0:
        return
    for i in range(m, 0, -1):
        if i > n:
            continue
        k = n - i
        for p_ in partitions_below(k, i):
            yield [i] + p_

def partitions(n):
    return partitions_below(n, n - 1)

if __name__ == '__main__':
    for p in partitions(10):
        print(" + ".join(p))