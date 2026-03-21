def factorial_poly(coeffs, x, n):
    p = coeffs[n] 
    for k in range(n - 1, -1, -1):
        p = p * (x - (n - 1 - k)) + coeffs[k]
    return p
coeffs = [1, 1, 1]
x = 3
n = 2

result = factorial_poly(coeffs, x, n)
expected = 1 + 1*x + 1*(x*(x-1))
print(f"Результат: {result}")  
print(f"Напрямую:  {expected}")
print(f"Совпадает: {result == expected}")
