def f(u, x):
    t = 1
    s = u[0]
    for i in range(1, len(u)):
        t = t * (x - (i - 1))
        s = s + u[i] * t
    return s
