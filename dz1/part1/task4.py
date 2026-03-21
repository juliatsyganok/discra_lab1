from class_polynom import Polynom

def limit_infty(f, g):
    df = f.deg()
    dg = g.deg()
    if df < dg:
        return 0
    if df == dg:
        return f.coef[-1] / g.coef[-1]
    return float("inf")

def limit_at_A(f, g, A):
    f_val = f(A) 
    g_val = g(A)
    if abs(g_val) > 1e-9:
        return f_val / g_val
    if abs(f_val) < 1e-9:
        f_reduced = gorner(f, A)
        g_reduced = gorner(g, A)
        return limit_at_A(f_reduced, g_reduced, A)  
    return float("inf")


def gorner(p, A):
    coeffs = p.coef[::-1]
    result = []
    rem = 0
    for c in coeffs:
        rem = rem * A + c 
        result.append(rem)

    result.pop()       
    result = result[::-1] 
    return Polynom(result)