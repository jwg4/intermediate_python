class FiniteField(object):
    def __init__(self, p):
        self.p = p

        class FFPoint(object):
            def __init__(self, n):
                self.n = n % p

            def __add__(self, x):
                return FFPoint(self.n + x.n)

            def __mult__(self, x):
                return FFPoint(self.n * x.n)

            def __eq__(self, x):
                return self.n == x.n

            def __str__(self):
                return "FFPoint(%d)" % (self.n, )

        self.FFPoint = FFPoint
