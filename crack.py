from generate import xs128p


def naive_predict(x1, x2):
    _, _, x3 = xs128p(x1, x2)
    return x3


def compare(s1, s2, predict):
    u1, u2, x1 = xs128p(s1, s2)
    v1, v2, x2 = xs128p(u1, u2)
    _, _, x3 = xs128p(v1, v2)
    p = predict(x1, x2)
    print "Prediction: %s Result: %s" % (bin(p), bin(x3))

if __name__ == '__main__':
    compare(1254, 2408201, naive_predict)
