# Atividade 01 

import numpy as np

def lu_pivot(A: np.ndarray):
    A = A.astype(float).copy()
    n = A.shape[0]
    P = np.eye(n)
    L = np.zeros((n, n))
    U = A.copy()

    for k in range(n):
        pivot = np.argmax(np.abs(U[k:, k])) + k
        if np.isclose(U[pivot, k], 0.0):
            raise np.linalg.LinAlgError("Matriz singular ou quase singular.")
        if pivot != k:
            U[[k, pivot], k:] = U[[pivot, k], k:]
            P[[k, pivot], :] = P[[pivot, k], :]
            if k > 0:
                L[[k, pivot], :k] = L[[pivot, k], :k]

        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]

    np.fill_diagonal(L, 1.0)
    return P, L, U

def lb(L: np.ndarray, B: np.ndarray) -> np.ndarray:
    n = L.shape[0]
    Y = np.zeros(n)
    for i in range(n):
        Y[i] = B[i] - np.dot(L[i, :i], Y[:i])
    return Y

def uy(U: np.ndarray, Y: np.ndarray) -> np.ndarray:
    n = U.shape[0]
    X = np.zeros(n)
    for i in reversed(range(n)):
        if np.isclose(U[i, i], 0.0):
            raise np.linalg.LinAlgError("U possui pivô nulo; sistema sem solução única.")
        X[i] = (Y[i] - np.dot(U[i, i + 1:], X[i + 1:])) / U[i, i]
    return X

def lu(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    P, L, U = lu_pivot(A)
    Pb = P @ B
    Y = lb(L, Pb)
    X = uy(U, Y)
    return X

def jacobi(A: np.ndarray, B: np.ndarray, k: int, TOL: float) -> np.ndarray:
    A = A.astype(float)
    B = B.astype(float)
    n = B.shape[0]
    X = np.zeros(n)
    D = np.diag(A)
    R = A - np.diagflat(D)

    for _ in range(k):
        X_new = (B - R @ X) / D
        if np.linalg.norm(X_new - X, ord=2) < TOL:
            return X_new
        X = X_new.copy()
    return X

def seidel(A: np.ndarray, B: np.ndarray, k: int, TOL: float) -> np.ndarray:
    A = A.astype(float)
    B = B.astype(float)
    n = B.shape[0]
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
    print("-- Atividade 1 --")

    A = np.array([
        [1, 1, 1],
        [4, 4, 2],
        [2, 1, -1]
    ], dtype=float)
    B = np.array([1, 2, 0], dtype=float)

    print("\nMatriz A:")
    print(A)
    print("\nVetor B:")
    print(B)

    print("\nSolução com NumPy:")
    print(np.linalg.solve(A, B))

    print("\nSolução com LU:")
    print(lu(A, B))

    print("\nSolução com Jacobi:")
    print(jacobi(A, B, k=100, TOL=1e-8))

    print("\nSolução com Seidel:")
    print(seidel(A, B, k=100, TOL=1e-8))

if __name__ == "__main__":
    main()
