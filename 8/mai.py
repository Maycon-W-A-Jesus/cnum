 # Atividades 1, 2, 3 e 4

import numpy as np

# 🔹 Método da Bisseção — Atividade 1
def bissecao(f, a, b, tol=1e-8, max_iter=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos")

    for _ in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tol or (b - a) / 2 < tol:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) / 2

# 🔹 Método de Gauss-Seidel — Atividades 2 e 3
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

# 🔹 Método de Newton-Raphson — Atividade 4
def f(T, E1, E2):
    T1, T2 = T
    f1 = (T1**4 + 0.06823*T1) - (T2**4 + 0.05848*T2) - E1
    f2 = (T1**4 + 0.05848*T1) - (2*T2**4 + 0.11696*T2) - E2
    return np.array([f1, f2])

def jacobian(T):
    T1, T2 = T
    df1_dT1 = 4*T1**3 + 0.06823
    df1_dT2 = -4*T2**3 - 0.05848
    df2_dT1 = 4*T1**3 + 0.05848
    df2_dT2 = -8*T2**3 - 0.11696
    return np.array([
        [df1_dT1, df1_dT2],
        [df2_dT1, df2_dT2]
    ])

def newton_raphson(E1, E2, T_init, tol=1e-8, max_iter=100):
    T = np.array(T_init, dtype=float)
    for _ in range(max_iter):
        F = f(T, E1, E2)
        J = jacobian(T)
        delta = np.linalg.solve(J, -F)
        T = T + delta
        if np.linalg.norm(delta, ord=2) < tol:
            break
    return T

# 🔹 Atividade 1 — Temperatura mínima da placa
def atividade1():
    E = 500.125
    K = 272.975

    def f1(T):
        return 5.67e-8 * T**4 + 0.4 * (T - K) - E

    T_minima = bissecao(f1, 273, 400)
    print("🔹 Atividade 1: Temperatura mínima da placa")
    print(f"T = {T_minima:.17f} K")

# 🔹 Atividade 2 — Tensões nominais dos reatores
def atividade2():
    A = np.array([
        [17, -2, -3],
        [-5, 21, -2],
        [-5, -5, 22]
    ], dtype=float)
    B = np.array([500, 200, 300], dtype=float)
    R = seidel(A, B)
    print("\n🔹 Atividade 2: Tensões nominais dos reatores")
    print(f"R1 = {R[0]:.6f}")
    print(f"R2 = {R[1]:.6f}")
    print(f"R3 = {R[2]:.6f}")

# 🔹 Atividade 3 — Corrente no resistor R3
def atividade3():
    A = np.array([
        [20.0, 10.0],
        [10.0, 20.0]
    ], dtype=float)
    B = np.array([100.0, 100.0], dtype=float)
    I = seidel(A, B)
    IR3 = I[0] - I[1]
    print("\n🔹 Atividade 3: Corrente no resistor R3")
    print(f"I1 = {I[0]:.4f}, I2 = {I[1]:.4f}")
    print(f"IR3 = {IR3:.4f} A")

# 🔹 Atividade 4 — Temperaturas de equilíbrio
def atividade4():
    E1 = 0.01753
    E2 = 0.00254
    T_init = [0.3, 0.2]
    T1, T2 = newton_raphson(E1, E2, T_init)
    print("\n🔹 Atividade 4: Temperaturas de equilíbrio")
    print(f"T1 = {T1:.5f}")
    print(f"T2 = {T2:.5f}")

# 🔹 Executar todas
if __name__ == "__main__":
    atividade1()
    atividade2()
    atividade3()
    atividade4()
