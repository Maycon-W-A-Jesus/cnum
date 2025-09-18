# Atividade 6
import numpy as np
import matplotlib.pyplot as plt
from algoritmos import bissecao

# Função da Atividade 6
def f6(x):
    F = 1e3       # Frequência em Hz
    L = 100e-3    # Indutância em H
    R = 1e3       # Resistência em Ohms
    T = 2 * np.pi * F * L / R
    A = np.atan(T)
    return np.sin(x - A) + np.sin(A) * np.exp(-x / T)

# Função para plotar
def plot(f, xi, xf, d=0.1, num_img=1):
    x_vals = np.arange(xi, xf, d)
    y_vals = f(x_vals)

    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.plot(x_vals, y_vals)
    plt.grid(True)
    plt.title("Visualização da função f(x)")
    plt.savefig(f"4/bissecao_{num_img}.png", dpi=120, bbox_inches="tight")
    plt.close()

# Função principal
def main():
    print("-- Atividade 6 --")
    a = 212 * np.pi / 180  # Limite inferior em radianos
    b = 213 * np.pi / 180  # Limite superior em radianos
    plot(f6, a, b, d=0.01, num_img=6)
    r, i = bissecao(f6, a, b, 1e-4, iter=100)
    r_deg = r * 180 / np.pi
    print(f"raiz = {r_deg:.4f}°, iterações = {i}")

if __name__ == "__main__":
    main()
