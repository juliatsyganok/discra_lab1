from class_polynom import Polynom

def gauss(G, F):
    n = len(F)
    m = len(G[0])
    mat = [G[i][:] + [F[i]] for i in range(n)]
    
    col = 0
    row = 0
    while row < n and col < m:
        pivot = None
        for i in range(row, n):
            if abs(mat[i][col]) > 1e-9:
                pivot = i
                break
        
        if pivot is None:
            col += 1 
            continue
        
        mat[row], mat[pivot] = mat[pivot], mat[row]
        div = mat[row][col]
        mat[row] = [x / div for x in mat[row]]
        for i in range(n):
            if i != row:
                factor = mat[i][col]
                mat[i] = [mat[i][j] - factor * mat[row][j] for j in range(m + 1)]
        row += 1
        col += 1
    A = [mat[i][m] for i in range(m)]
    return A

G = [[2, 1], [1, 3]]
F = [5, 10]
A = gauss(G, F)
print(A)