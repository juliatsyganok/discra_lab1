def f(a, x, y):
    s = 0
    for r in a:
        t = 0
        for c in r:
            t = t * y + c
        s = s * x + t
    return s
