def f(a, x, x0):
    y = x + x0
    r = 0
    for c in a:
        r = r * y + c
    return r
