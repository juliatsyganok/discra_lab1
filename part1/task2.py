import math
from part1.class_polynom import Polynom

def proiz(poly):
    if poly.deg() == 0:
        return Polynom([0])
    coef = [(i) * poly.coef[i] for i in range(1, len(poly.coef))]
    return Polynom(coef)


def bas(f, a):
    coef = []
    p = f
    for k in range(f.deg() + 1):
        coef.append(p(a) / math.factorial(k))
        p = proiz(p)
    return coef

f = Polynom([0, 0, 1])

print(bas(f, 1))