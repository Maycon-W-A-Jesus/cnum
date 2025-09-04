# Atividade 03

import numpy as np
import matplotlib.pyplot as plt

# Função f(x) = e^(-x²) - 2x
def f3(x):
    return np.exp(-x**2) - 2 * x

# Função iterativa g(x) = 0.5 * e^(-x²)
def g3(x):
    return 0.5 * np.exp(-x**2)

# Método de ponto fixo
def pontofixo(a, g, TOL=1e-8):
    x = g(a)
    count = 1
    while abs(x - a) > TOL:
        a = x
        x = g(a)
        count += 1
    return x, count

# Função para plotar f3(x)
def plot_f3(xi, xf, d=0.01, raiz=None):
    x_vals = np.arange(xi, xf, d)
    y_vals = f3(x_vals)
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.plot(x_vals, y_vals, label="f(x) = e^(-x²) - 2x", color="blue")
    if raiz:
        plt.plot(raiz, f3(raiz), 'ro', label=f"Raiz ≈ {raiz:.7f}")
    plt.grid(True)
    plt.title("Função f(x) da Atividade 03")
    plt.legend()
    plt.savefig("atividade03_funcao.png", dpi=120, bbox_inches="tight")
    plt.close()

# Função principal
def main():
    print("-- Atividade 03: Método do Ponto Fixo --")
    a = 0.5  # chute inicial
    raiz, iteracoes = pontofixo(a, g3, TOL=1e-7)
    print(f"Raiz aproximada = {raiz:.7f}, Iterações = {iteracoes}")
    plot_f3(0, 1, d=0.01, raiz=raiz)

if __name__ == "__main__":
    main()
