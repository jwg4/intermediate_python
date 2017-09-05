from collections import defaultdict

from poly import Polynomial
from sets import subsets_k
from sets import subsets_no_more_than


POLY_LISTS = [
    [1, 1],
    [1, 0, 1],
    [1, -1, 1, -1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, -1, 0, 1, 0, -1, 0, 1]
]

POLYS = [ Polynomial(l) for l in POLY_LISTS ]


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


def combine_w_symmetry(sets, symmetrical=True):
    if not sets:
        yield [[], []]
        return

    s = sets[0]
    tail = sets[1:]
    for left, right, is_sym in s:
        if is_sym:
            for l_tail, r_tail in combine_w_symmetry(tail, True):
                yield [left + l_tail, right + r_tail]
        else:
            for l_tail, r_tail in combine_w_symmetry(tail, False):
                if symmetrical:
                    yield [left + l_tail, right + r_tail]
                else:
                    yield [left + l_tail, right + r_tail]
                    yield [right + l_tail, left + r_tail]
     

 
def split(polys):
    by_height = split_by_height(polys)
    splits = [ list(split_set(by_height[x])) for x in by_height ]
    combinations = combine_w_symmetry(splits, True)
    return list(combinations)


if __name__ == '__main__':
    x = split(POLYS)
    print len(x)
    print x
