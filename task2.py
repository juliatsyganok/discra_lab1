import math
from class_polynom import Polynom

def derivative(poly):
    if poly.degree() == 0:
        return Polynom([0])

    coeffs = [(i)*poly.coeffs[i] for i in range(1,len(poly.coeffs))]
    return Polynom(coeffs)


def shift_basis(f,a):
    coeffs=[]
    p=f

    for k in range(f.degree()+1):
        coeffs.append(p(a)/math.factorial(k))
        p=derivative(p)

    return coeffs