from math import comb

def change_center(coeffs,a,B):
    n=len(coeffs)
    res=[0]*n

    d=B-a

    for k in range(n):
        for i in range(k+1):
            res[i]+=coeffs[k]*comb(k,i)*(d**(k-i))

    return res