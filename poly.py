class Polynomial(object):
    def __init__(self, coeffs):
        self.coeffs = coeffs
    
    @staticmethod
    def _monomial(n):
        if n == 0:
            return ""
        if n == 1:
            return "x"
        return "x**%d" % (n, )

    @staticmethod
    def _monomial_a(a, n):
        if a == 0:
            return []
        elif n == 0:
            return ["%d" % a]
        elif a == 1:
            return [Polynomial._monomial(n)]
        else:
            return ["%d%s" % (a, Polynomial._monomial(n))]
        

    def __str__(self):
        l = []
        c = 0
        for a in self.coeffs:
            l.extend(Polynomial._monomial_a(a, c))
            c = c + 1
        return " + ".join(l[::-1])
