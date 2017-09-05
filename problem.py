from collections import defaultdict

from poly import Polynomial
from sets import subsets_k
from sets import subsets_no_more_than


polys = [
    [1, 1],
    [1, 0, 1],
    [1, -1, 1, -1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, -1, 0, 1, 0, -1, 0, 1]
]


def split_set(polys):
    yield [polys, polys, True]
    n = len(polys)
    for double in subsets_no_more_than(polys):
        if double != []:
            start = polys.index(double[0])
            remainder = polys[start+1:]
            for zero in subsets_k(remainder, len(double)):
                left = [ p for p in polys if p not in zero ] + double
                right = [ p for p in polys if p not in double ] + zero
                yield [left, right, False]


def split_by_height(polys):
    d = defaultdict(list)
    for p in polys:
        d[p.height].append(p)
    return dict(d)


def split(polys):
    by_height = split_by_height(polys)
    splits = [ split_set(by_height[x]) for x in by_height ]
