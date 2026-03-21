def horner_complex(coeffs, z):
    p = 0
    for c in reversed(coeffs):
        p = p * z + c
    return p


def scheme3(coeffs, z):
    x, y = z.real, z.imag
    y2 = y * y
    even = coeffs[0::2] 
    odd  = coeffs[1::2] 
    p = 0
    for c in reversed(even):
        p = p * y2 + c
    q = 0
    for c in reversed(odd):
        q = q * y2 + c

    return complex(p + x*q, y*q) 

coeffs = [1, 2, 3, 4] 
z = complex(1, 2)

print(horner_complex(coeffs, z)) 
print(scheme3(coeffs, z))       
print(1 + 2*z + 3*z**2 + 4*z**3) 