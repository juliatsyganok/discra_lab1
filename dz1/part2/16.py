def short_division(digits, v, b=10):
    r = 0         
    quotient = []  

    for u in digits:
        cur = r * b + u        
        w = cur // v          
        r = cur % v         
        quotient.append(w)

    while len(quotient) > 1 and quotient[0] == 0:
        quotient.pop(0)

    return quotient, r



digits = [1, 2, 3, 4]
q, r = short_division(digits, 3)
print(f"1234 / 3 = {''.join(map(str,q))} остаток {r}")  # 411 ост 1
