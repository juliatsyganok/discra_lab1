def limit_infty(f,g):

    df=f.degree()
    dg=g.degree()

    if df < dg:
        return 0

    if df == dg:
        return f.coef[-1]/g.coef[-1]

    return float("inf")

def limit_at(f,g,A):

    if g(A)!=0:
        return f(A)/g(A)

    return None