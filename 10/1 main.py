import numpy as np
import matplotlib.pyplot as plt
import os

def regressao(x, y, v):
    V = v(x)
    Vt = V.T
    A = np.linalg.inv(Vt @ V) @ (Vt @ y)
    return A

def plot_regressao(x, y, v, A, nome_arquivo, titulo):
    x_vals = np.linspace(min(x) - 0.25, max(x) + 0.25, 400)
    y_vals = np.zeros_like(x_vals, dtype=float)
    for p, ap in enumerate(A):
        y_vals += ap * (x_vals**p)
    plt.style.use("seaborn-v0_8")
    plt.figure(figsize=(7, 4))
    plt.scatter(x, y, color="blue", label="Pontos dados")
    plt.plot(x_vals, y_vals, color="red", label="Ajuste f(x)")
    plt.title(titulo)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle=":")
    plt.legend()
    plt.tight_layout()
    os.makedirs("10", exist_ok=True)
    plt.savefig(f"10/{nome_arquivo}", dpi=120, bbox_inches="tight")
    plt.close()

def atividade1():
    x = np.array([-0.35, 0.15, 0.23, 0.35])
    y = np.array([0.20, -0.50, 0.54, 0.70])
    v = lambda x: np.column_stack((np.ones(len(x)), x))
    A = regressao(x, y, v)
    print(f"Atividade 1: f(x) = {A[0]:.2f} + {A[1]:.2f}x")
    plot_regressao(x, y, v, A, "regressao_1.png", "Atividade 1: Ajuste Linear")

def atividade2():
    x = np.array([-1.94, -1.44, 0.93, 1.39])
    y = np.array([1.02, 0.59, -0.28, -1.04])
    v = lambda x: np.column_stack((np.ones(len(x)), x))
    A = regressao(x, y, v)
    f1 = A[0] + A[1]*1
    print(f"Atividade 2: f(x) = {A[0]:.8f} + {A[1]:.8f}x, f(1) = {f1:.7f}")
    plot_regressao(x, y, v, A, "regressao_2.png", "Atividade 2: Ajuste Linear")

def atividade3():
    x = np.array([0.01, 1.02, 2.04, 2.95, 3.55])
    y = np.array([1.99, 4.55, 7.20, 9.51, 10.82])
    v = lambda x: np.column_stack((x**2, x, np.ones(len(x))))
    A = regressao(x, y, v)
    print(f"Atividade 3: f(x) = {A[0]:.7f}x² + {A[1]:.7f}x + {A[2]:.7f}")
    plot_regressao(x, y, v, A, "regressao_3.png", "Atividade 3: Ajuste Quadrático")

def atividade4a():
    x = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    y = np.array([31, 35, 37, 33, 28, 20, 16, 15, 18, 23, 31])
    v = lambda x: np.column_stack((np.ones(len(x)), np.sin(2*np.pi*x), np.cos(2*np.pi*x)))
    A = regressao(x, y, v)
    print(f"Atividade 4a: f(x) = {A[0]:.6f} + {A[1]:.7f}sin(2πx) + {A[2]:.7f}cos(2πx)")
    plot_regressao(x, y, v, A, "regressao_4a.png", "Atividade 4a: Ajuste Trigonométrico")

def atividade4b():
    x = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    y = np.array([31, 35, 37, 33, 28, 20, 16, 15, 18, 23, 31])
    v = lambda x: np.column_stack((np.ones(len(x)), x, x**2, x**3))
    A = regressao(x, y, v)
    print(f"Atividade 4b: f(x) = {A[0]:.6f} + {A[1]:.6f}x + {A[2]:.6f}x² + {A[3]:.6f}x³")
    plot_regressao(x, y, v, A, "regressao_4b.png", "Atividade 4b: Ajuste Polinomial de Grau 3")

def main():
    atividade1()
    atividade2()
    atividade3()
    atividade4a()
    atividade4b()

if __name__ == "__main__":
    main()
