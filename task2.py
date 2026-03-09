import math
from class_polynom import Polynom

def derivative(poly):
    if poly.degree() == 0:
        return Polynom([0])

    coef = [(i)*poly.coef[i] for i in range(1,len(poly.coef))]
    return Polynom(coef)


def shift_basis(f,a):
    coef=[]
    p=f

    for k in range(f.degree()+1):
        coef.append(p(a)/math.factorial(k))
        p=derivative(p)

    return coef