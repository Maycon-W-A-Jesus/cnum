import numpy as np

# Métodos numéricos
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
    Xk = np.zeros(n)

    D = np.diag(A)
    if np.any(D == 0):
        raise ValueError("A possui elementos diagonais nulos; Jacobi pode falhar.")

    R = A - np.diagflat(D)

    for _ in range(k):
        Xk = (B - R @ X) / D
        if np.linalg.norm(Xk - X, ord=2) < TOL:
            return Xk
        X = Xk.copy()
    return X

def seidel(A: np.ndarray, B: np.ndarray, k: int, TOL: float) -> np.ndarray:
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
            return X
    return X

# Sistema da Atividade 4
def montar_sistema(R1, R2, R3, R4, R5, R6, R7, R8, V1):
    A = np.array([
        [-1/R1 - 1/R2 - 1/R5, 0, 0, 1/R2],
        [1/R2, -1/R2 - 1/R3 - 1/R6, 1/R3, 0],
        [0, 1/R3, -1/R3 - 1/R4 - 1/R7, 1/R4],
        [0, 0, 1/R4, -1/R4 - 1/R8]
    ], dtype=float)
    B = np.array([
        -V1 / R1,
        0,
        0,
        0
    ], dtype=float)
    return A, B

# Execução principal
def main():
    V1 = 127
    TOL = 1e-5
    k = 100

    print("\n🔹 Caso A:")
    A, B = montar_sistema(2, 2, 2, 2, 100, 100, 100, 50, V1)
    print("LU:", np.round(lu(A, B), 4))
    print("Jacobi:", np.round(jacobi(A, B, k, TOL), 4))
    print("Seidel:", np.round(seidel(A, B, k, TOL), 4))

    print("\n🔹 Caso B:")
    A, B = montar_sistema(2, 2, 2, 2, 50, 100, 100, 100, V1)
    print("LU:", np.round(lu(A, B), 4))
    print("Jacobi:", np.round(jacobi(A, B, k, TOL), 4))
    print("Seidel:", np.round(seidel(A, B, k, TOL), 4))

if __name__ == "__main__":
    main()
