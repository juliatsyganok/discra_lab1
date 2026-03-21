def horner_2d(coeffs, x, y, n):
    result = 0
    for j in range(n, -1, -1):
        row = 0
        for i in range(n - j, -1, -1):
            row = row * x + coeffs[i][j] 
        result = result * y + row       

    return result

n = 2
coeffs = [[0]*3 for _ in range(3)]
coeffs[0][0] = 1
coeffs[1][0] = 2
coeffs[0][1] = 3
coeffs[2][0] = 4
coeffs[1][1] = 5
coeffs[0][2] = 6

x, y = 2, 3
result = horner_2d(coeffs, x, y, n)