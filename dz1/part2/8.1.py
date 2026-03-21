def complex_div_7(a0, a1, b0, b1):
    m1 = a0 * b0
    m2 = a1 * b1
    m3 = a1 * b0
    m4 = a0 * b1
    m5 = b0 * b0
    m6 = b1 * b1
    inv = 1 / (m5 + m6)  
    return (m1 + m2) * inv, (m3 - m4) * inv



def complex_div_6(a0, a1, b0, b1):
    m1 = a0 * b0
    m2 = a1 * b1
    m3 = (a0 + a1) * (b0 + b1)
    m4 = b0 * b0
    m5 = b1 * b1
    inv = 1 / (m4 + m5) 
    return (m1 + m2) * inv, (m3 - m1 - m2) * inv
