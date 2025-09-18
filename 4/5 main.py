# Atividade 5
import numpy as np
import matplotlib.pyplot as plt
import os
from algoritmos import bissecao  # Certifique-se de que algoritmos.py está no mesmo diretório

# Parâmetros do problema
d = 500         # distância entre torres (m)
f_max = 50      # flecha máxima permitida (m)

# Função da catenária
def f5(C):
    return C * (np.cosh(d / (2 * C)) - 1) - f_max

# Função para plotar e salvar imagem
def plot(f, xi, xf, d=1, num_img=5):
    x_vals = np.linspace(xi, xf, 500)
    y_vals = [f(x) for x in x_vals]

    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.plot(x_vals, y_vals, label='f(C)')
    plt.grid(True)
    plt.title("Visualização da função f(C)")
    plt.xlabel("C (m)")
    plt.ylabel("f(C)")
    plt.legend()

    os.makedirs("5", exist_ok=True)
    plt.savefig(f"5/bissecao_{num_img}.png", dpi=120, bbox_inches="tight")
    plt.close()

# Função principal
def main():
    print("-- Atividade 5 --")
    
    # Plot da função f(C)
    plot(f5, 550, 650, num_img=5)

    # Encontrar raiz usando bisseção
    C_sol, iteracoes = bissecao(f5, 550, 650, 1e-6)

    # Calcular comprimento total do cabo
    L = 2 * C_sol * np.sinh(d / (2 * C_sol))

    # Exibir resultados
    print(f"Distância entre torres: {d} m")
    print(f"Flecha máxima permitida: {f_max} m")
    print(f"Constante da catenária C ≈ {C_sol:.4f} m")
    print(f"Comprimento total do cabo L ≈ {L:.4f} m")
    print(f"Número de iterações realizadas: {iteracoes}")

if __name__ == "__main__":
    main()
