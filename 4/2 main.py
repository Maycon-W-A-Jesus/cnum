import numpy as np
import matplotlib.pyplot as plt

from algoritmos import bissecao

#√x = cos(x)
# Função f(x) = sqrt(x) - cos(x)
def f2(x):
    return x**(1/2) - np.cos(x)

def plot(f, xi, fx, d=0.1, num_imag=1):

    x_vals = np.arange(xi, fx, d)
    y_vals = f(x_vals)

    plt.axhline(0, color="black", linewidth=1)  # eixo x
    plt.axvline(0, color="black", linewidth=1)  # eixo y
    plt.plot(x_vals, y_vals)
    plt.grid(True)
    plt.title("Visualização da função f(x)")

    # Salvar gráfico como imagem
    plt.savefig(f"4/bissecao_{num_imag}.png", dpi=120, bbox_inches="tight")
    plt.close()

def main():
    print("-- Atividade 2 --")
    plot(f2, 0, 1, num_imag=2)
    r, i = bissecao(f2, 0, 4, 1e-4, iter=4)
    print(f"raiz ≈ {r:.4f} , iterações = {i}")

if __name__ == "__main__":
    main()

