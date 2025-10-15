import numpy as np
from scipy.optimize import approx_fprime

# Método da Bisseção
def bissecao(f, a, b, TOL=1e-8, iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("Intervalo inválido: f(a) * f(b) > 0")
    i = 0
    while (b - a) / 2 > TOL and i < iter:
        c = (a + b) / 2.0
        if abs(f(c)) < TOL:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        i += 1
    return (a + b) / 2.0

# Método de Gauss-Seidel
def seidel(A, B, k=100, TOL=1e-8):
    A = A.astype(float)
    B = B.astype(float)
    n = B.shape[0]
    X = np.zeros(n)
    for _ in range(k):
        Xk = X.copy()
        for i in range(n):
            s1 = np.dot(A[i, :i], X[:i])
            s2 = np.dot(A[i, i + 1:], Xk[i + 1:])
            X[i] = (B[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(X - Xk, ord=2) < TOL:
            break
    return X

# Jacobiana Numérica
def JN(x, F, eps=1e-8):
    x = np.asarray(x, dtype=float)
    n = x.size
    Jnum = np.zeros((n, n), dtype=float)
    for i in range(n):
        def fi(v, i=i):
            return F(v)[i]
        Jnum[i, :] = approx_fprime(x, fi, epsilon=eps)
    return Jnum

# Método de Newton-Raphson Numérico
def newton_numerico(x0, F, TOL=1e-8, iter=100):
    x = x0.copy()
    for _ in range(iter):
        J = JN(x, F)
        delta = np.linalg.solve(J, F(x))
        x_new = x - delta
        if np.linalg.norm(x_new - x, ord=2) < TOL:
            return x_new
        x = x_new
    return x
