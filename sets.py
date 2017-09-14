def subsets(s):
    return subsets_no_more_than(s, len(s))


def subsets_no_more_than(s, k=None):
    n = len(s)
    if k is None:
        k = n / 2
    for i in range(0, 2**n):
        format_string = '0%db' % n
        bin_string = format(i, format_string)
        indices = [ i for i in range(0, n) if bin_string[i] == '1' ]
        if len(indices) <= k:
            yield [ s[i] for i in indices ]


def subsets_k(s, k):
    if k == 0:
        yield []
    n = len(s)
    if n < k:
        return
    for i in range(0, n):
        tails = subsets_k(s[i+1:], k-1)
        for tail in tails:
            yield [s[i]] + tail


def multi_subsets(s):
    keys = s.keys()
    if not keys:
        yield {}
        return
    
    key = keys[0]

    sc = s.copy()
    n = sc.pop(key)
    for ss in multi_subsets(sc):
        yield ss.copy()
        for i in range(1, n + 1):
            d = {key: i}
            d.update(ss)
            yield d
        
