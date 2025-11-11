import numpy as np
import matplotlib.pyplot as plt

def derivada_posterior(x, y, i):
    return (y[i+1] - y[i]) / (x[i+1] - x[i])

def derivada_anterior(x, y, i):
    return (y[i] - y[i-1]) / (x[i] - x[i-1])

def derivada_central(x, y, i):
    return (y[i+1] - y[i-1]) / (x[i+1] - x[i-1])

def grafico_ganho(vi, vo):
    plt.figure(figsize=(7, 4))
    plt.plot(vi, vo, 'o-', label='Dados medidos')
    V = np.column_stack((vi, vi**3))
    A = np.linalg.inv(V.T @ V) @ (V.T @ vo)
    vi_vals = np.linspace(min(vi), max(vi), 200)
    vo_ajuste = A[0]*vi_vals + A[1]*vi_vals**3
    plt.plot(vi_vals, vo_ajuste, 'r--', label='Ajuste vo = a1*vi + a3*vi³')
    plt.xlabel('vi (V)')
    plt.ylabel('vo (V)')
    plt.title('Ganho do amplificador')
    plt.grid(True, linestyle=':')
    plt.legend()
    plt.tight_layout()
    plt.savefig("11/ganho_amplificador.png", dpi=120)
    plt.close()
    return A

def atividade2():
    print("-- Atividade 2 --")
    vi = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
    vo = np.array([0.0, 1.05, 1.83, 2.69, 3.83, 4.56, 5.49, 6.56, 6.11, 7.06, 8.29])

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

    A = grafico_ganho(vi, vo)
    a1, a3 = A
    f_ajustada = lambda x: a1 + 3*a3*x**2
    print("\nd) Derivada da função ajustada vo = a1*vi + a3*vi^3")
    print(f"Coeficientes: a1 = {a1:.8f}, a3 = {a3:.8f}")
    print(f"Ganho em vi = 1.0: {f_ajustada(1.0):.2f}")
    print(f"Ganho em vi = 4.5: {f_ajustada(4.5):.2f}")

def main():
    atividade2()

if __name__ == "__main__":
    main()
