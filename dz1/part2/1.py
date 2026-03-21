def eval_odd_poly(coeffs, x):
    y = x ** 2 
    p = 0
    for c in reversed(coeffs):
        p = p * y + c 
    return x * p  

coeffs = [1, 2, 3]
x = 2.0

result = eval_odd_poly(coeffs, x)
expected = 3*x**5 + 2*x**3 + 1*x

print(f"Наш метод: {result}")    
print(f"Напрямую:  {expected}")  
print(f"Совпадает: {abs(result - expected) < 1e-9}")