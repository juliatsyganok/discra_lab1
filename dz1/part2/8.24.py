def f(a, v, b):
    r = 0
    q = []
    for x in a:
        r = r * b + x
        q.append(r // v)
        r = r % v
    return q, r
