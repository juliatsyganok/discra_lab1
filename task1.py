import numpy as np
from class_polynom import Polynom

def in_span(f, gs):
    max_deg = max([f.deg()] + [g.deg() for g in gs])
    def pad(p):
        return p.coef + [0] * (max_deg + 1 - len(p.coef))
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
    
f = Polynom([1, 3, 2])
g1 = Polynom([1, 1])
g2 = Polynom([0, 1, 1])

print(in_span(f, [g1, g2]))