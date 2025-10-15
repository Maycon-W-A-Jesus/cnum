# Atividade 4 
# Equilíbrio térmico em sistema solar (Newton-Raphson)

import numpy as np

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

# Dados experimentais
E1 = 0.01753
E2 = 0.00254

# Chute inicial
T_init = [0.3, 0.2]

# Resolvendo
T1, T2 = newton_raphson(E1, E2, T_init)

if __name__ == "__main__":
    print("Temperaturas de equilíbrio")
    print(f"T1 = {T1:.5f}")
    print(f"T2 = {T2:.5f}")
