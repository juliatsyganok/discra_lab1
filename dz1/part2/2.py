def horner_shift(coeffs, x0):
    p = [coeffs[-1]] 

    for c in reversed(coeffs[:-1]):
        new_p = [0] * (len(p) + 1)
        for i, a in enumerate(p):
            new_p[i + 1] += a    
            new_p[i]     += a * x0 
        new_p[0] += c   
        p = new_p

    return p

print(horner_shift([1, 2, 1], 1)) 
print(horner_shift([0, 0, 0, 1], 2))  