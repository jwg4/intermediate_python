from math_helpers import eea


class FiniteField(object):
    def __init__(self, p):
        self.p = p

        class FFPoint(object):
            def __init__(self, n):
                self.n = n % p

            @property
            def inv(self):
                d, m, n = eea(self.n, p)
                return m
 
            def __add__(self, x):
                return FFPoint(self.n + x.n)

            def __mul__(self, x):
                return FFPoint(self.n * x.n)

            def __div__(self, x):
                return FFPoint(self.n * x.inv)

            def __eq__(self, x):
                return self.n == x.n

            def __str__(self):
                return "FFPoint(%d)" % (self.n, )

            def __repr__(self):
                return "FFPoint(%d)" % (self.n, )

        self.FFPoint = FFPoint
