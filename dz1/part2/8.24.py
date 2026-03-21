def fast_convolution(f, g, k):
    if k == 0:
        return [f[0] * g[0]]
    m = 2 ** (k - 1)
    f0 = [f[i] + f[i + m] for i in range(m)]  
    f1 = [f[i] - f[i + m] for i in range(m)]   
    g0 = [g[i] + g[i + m] for i in range(m)]
    g1 = [g[i] - g[i + m] for i in range(m)]
    h0 = fast_convolution(f0, g0, k - 1)
    h1 = fast_convolution(f1, g1, k - 1)

    return [(h0[i] + h1[i]) / 2 for i in range(m)] + \
           [(h0[i] - h1[i]) / 2 for i in range(m)]


f = [1, 2, 3, 4]
g = [1, 0, 1, 0]

print(fast_convolution(f, g, 2)) 