from part1.class_polynom import Polynom

def limit_infty(f, g):
    df = f.deg()
    dg = g.deg()
    if df < dg:
        return 0
    if df == dg:
        return f.coef[-1] / g.coef[-1]
    return float("inf")


f = Polynom([1,0,1])
g = Polynom([1,1])

print(limit_infty(f, g))