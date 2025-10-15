# Atividade 3 
# Corrente no resistor R3 usando Gauss-Seidel

import numpy as np

def seidel(A, B, k=100, TOL=1e-8):
    A = A.astype(float)
    B = B.astype(float)
    n = len(B)
    X = np.zeros(n)

    for _ in range(k):
        X_old = X.copy()
        for i in range(n):
            soma = np.dot(A[i, :i], X[:i]) + np.dot(A[i, i+1:], X[i+1:])
            X[i] = (B[i] - soma) / A[i, i]
        if np.linalg.norm(X - X_old, ord=2) < TOL:
            break
    return X

# Sistema equivalente do circuito
A = np.array([
    [20.0, 10.0],
    [10.0, 20.0]
], dtype=float)

B = np.array([100.0, 100.0], dtype=float)

# Resolvendo com Gauss-Seidel
I = seidel(A, B, k=100, TOL=1e-8)

# Corrente no resistor R3 é a diferença entre I1 e I2
IR3 = I[0] - I[1]

if __name__ == "__main__":
    print(f"I1 = {I[0]:.4f}, I2 = {I[1]:.4f}")
    print("Corrente no resistor R3")
    print(f"IR3 = {IR3:.4f} A")

    
