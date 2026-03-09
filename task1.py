import numpy as np
from class_polynom import Polynom

def in_span(f, gs):
    max_deg = max([f.degree()] + [g.degree() for g in gs])

    def pad(p):
        return p.coeffs + [0]*(max_deg+1-len(p.coeffs))

    F = np.array(pad(f))

    G = np.array([pad(g) for g in gs]).T

    try:
        A = np.linalg.lstsq(G, F, rcond=None)[0]

        if np.allclose(G @ A, F):
            return True, A
        else:
            return False, None

    except:
        return False, None