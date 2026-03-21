def f(a, b, c, d):
    p1 = a * c
    p2 = b * d
    p3 = (a + b) * (c + d)
    r = p1 - p2
    i = p3 - p1 - p2
    return r, i
