from math import comb

def B_a(coef, a, B):
    n = len(coef)
    res = [0] * n
    d = B - a
    for k in range(n):
        for i in range(k + 1):
            res[i] += coef[k] * comb(k, i) * (d ** (k - i))
    return res

coef = [1, 2, 1]

print(B_a(coef, 1, 0))