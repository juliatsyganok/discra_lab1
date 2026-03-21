def f(a0, a1, b0, b1):
    d = b0 * b0 + b1 * b1
    r = (a0 * b0 + a1 * b1) / d
    i = (a1 * b0 - a0 * b1) / d
    return r, i
