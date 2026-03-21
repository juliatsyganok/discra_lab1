def complex_mul(a, b, c, d):
    m1 = a * c     
    m2 = b * d   
    m3 = (a + b) * (c + d)  
    re = m1 - m2  
    im = m3 - m1 - m2  
    return re, im



a, b, c, d = 3, 2, 1, 4 
re, im = complex_mul(a, b, c, d)
print(f"Результат: {re} + {im}i")    
print(f"Проверка:  {(3+2j)*(1+4j)}")   