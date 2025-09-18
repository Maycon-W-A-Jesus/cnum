# Atividade 03

import numpy as np

def jacobi(A, B, k, TOL):
    n = len(B)
    X = np.zeros(n)
    D = np.diag(A)
    R = A - np.diagflat(D)

    for _ in range(k):
        X_new = (B - R @ X) / D
        if np.linalg.norm(X_new - X, ord=2) < TOL:
            return X_new
        X = X_new.copy()
    return X

def seidel(A, B, k, TOL):
    n = len(B)
    X = np.zeros(n)

    for _ in range(k):
        X_old = X.copy()
        for i in range(n):
            s1 = np.dot(A[i, :i], X[:i])
            s2 = np.dot(A[i, i + 1:], X_old[i + 1:])
            X[i] = (B[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(X - X_old, ord=2) < TOL:
            return X
    return X

def main():
    print("-- Atividade 3 (corrigida) --")

    A = np.array([
        [4, 0, 1],
        [1, 10, 3],
        [2, 1, 4]
    ], dtype=float)

    B = np.array([6, 27, 12], dtype=float)

    k = 100
    TOL = 1e-3

    X_jacobi = jacobi(A, B, k, TOL)
    X_seidel = seidel(A, B, k, TOL)

    print("\nSolução com Jacobi:")
    print(np.round(X_jacobi, 4))

    print("\nSolução com Gauss-Seidel:")
    print(np.round(X_seidel, 4))

if __name__ == "__main__":
    main()
