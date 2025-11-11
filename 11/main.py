import numpy as np
from algoritmos import dp, dr, dc

def atividade1():
    print("-- Atividade 1 --")
    h1 = 1e-2
    h2 = 1e-3
    eps = np.finfo(float).eps

    print("\nDerivadas para f(x) = sin(x) em x = 2")
    f = lambda x: np.sin(x)
    print(f"Progressiva: h={h1} → {dp(f, 2, h1):.5f}, h={h2} → {dp(f, 2, h2):.5f}")
    print(f"Regressiva:  h={h1} → {dr(f, 2, h1):.5f}, h={h2} → {dr(f, 2, h2):.5f}")
    print(f"Central:     h={h1} → {dc(f, 2, h1):.5f}, h={h2} → {dc(f, 2, h2):.5f}")
    print(f"Exata: cos(2) = {np.cos(2):.5f}")

    print("\nDerivadas para f(x) = e^(-x) em x = 1")
    f = lambda x: np.exp(-x)
    print(f"Progressiva: h={h1} → {dp(f, 1, h1):.5f}, h={h2} → {dp(f, 1, h2):.5f}")
    print(f"Regressiva:  h={h1} → {dr(f, 1, h1):.5f}, h={h2} → {dr(f, 1, h2):.5f}")
    print(f"Central:     h={h1} → {dc(f, 1, h1):.5f}, h={h2} → {dc(f, 1, h2):.5f}")
    print(f"Exata: -e^(-1) = {-np.exp(-1):.5f}")

def atividade2():
    print("\n-- Atividade 2 --")
    vi = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
    vo = np.array([0.0, 1.05, 1.83, 2.69, 3.83, 4.56, 5.49, 6.56, 6.11, 7.06, 8.29])

    def derivada_posterior(x, y, i):
        return (y[i+1] - y[i]) / (x[i+1] - x[i])

    def derivada_anterior(x, y, i):
        return (y[i] - y[i-1]) / (x[i] - x[i-1])

    def derivada_central(x, y, i):
        return (y[i+1] - y[i-1]) / (x[i+1] - x[i-1])

    idx_1 = np.where(vi == 1.0)[0][0]
    idx_2 = np.where(vi == 4.5)[0][0]

    print("\nGanho em vi = 1.0")
    print(f"a) Posterior: {derivada_posterior(vi, vo, idx_1):.2f}")
    print(f"b) Anterior:  {derivada_anterior(vi, vo, idx_1):.2f}")
    print(f"c) Central:   {derivada_central(vi, vo, idx_1):.2f}")

    print("\nGanho em vi = 4.5")
    print(f"a) Posterior: {derivada_posterior(vi, vo, idx_2):.2f}")
    print(f"b) Anterior:  {derivada_anterior(vi, vo, idx_2):.2f}")
    print(f"c) Central:   {derivada_central(vi, vo, idx_2):.2f}")

    # Ajuste vo = a1*vi + a3*vi^3
    V = np.column_stack((vi, vi**3))
    A = np.linalg.inv(V.T @ V) @ (V.T @ vo)
    a1, a3 = A
    f_ajustada = lambda x: a1 + 3*a3*x**2

    print("\nd) Derivada da função ajustada vo = a1*vi + a3*vi^3")
    print(f"Coeficientes: a1 = {a1:.8f}, a3 = {a3:.8f}")
    print(f"Ganho em vi = 1.0: {f_ajustada(1.0):.2f}")
    print(f"Ganho em vi = 4.5: {f_ajustada(4.5):.2f}")

def main():
    atividade1()
    atividade2()

if __name__ == "__main__":
    main()
