class Polynom:
    def __init__(self, coef):
        while len(coef) > 1 and coef[-1] == 0:
            coef.pop()
        self.coef = coef

    def deg(self):
        return len(self.coef) - 1

    def __call__(self, x):
        result = 0
        for c in reversed(self.coef):
            result = result * x + c
        return result

    def __add__(self, other):
        n = max(len(self.coef), len(other.coef))
        res = [0] * n

        for i in range(n):
            a = self.coef[i] if i < len(self.coef) else 0
            b = other.coef[i] if i < len(other.coef) else 0
            res[i] = a + b

        return Polynom(res)

    def __mul__(self, other):
        res = [0]*(len(self.coef)+len(other.coef)-1)

        for i,a in enumerate(self.coef):
            for j,b in enumerate(other.coef):
                res[i+j] += a*b

        return Polynom(res)

    def scale(self, k):
        return Polynom([k*c for c in self.coef])

    def __repr__(self):
        return f"Polynom({self.coef})"