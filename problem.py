from collections import defaultdict

from poly import Polynomial


polys = [
    [1, 1],
    [1, 0, 1],
    [1, -1, 1, -1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, -1, 0, 1, 0, -1, 0, 1]
]


def split_set(polys):
    yield([polys, polys, True])


def split_by_height(polys):
    d = defaultdict(list)
    for p in polys:
        d[p.height].append(p)
    return dict(d)


def split(polys):
    by_height = split_by_height(polys)
    splits = [ split_set(by_height[x]) for x in by_height ]
