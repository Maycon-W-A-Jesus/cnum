#Atividade 3
import numpy as np
import matplotlib.pyplot as plt
import os

# Função alvo
def f(x):
    return 5 * np.sin(x**2) - np.exp(x / 10)

# Método da bisseção
def bissecao(f, a, b, tol, iter_max=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("Não há mudança de sinal no intervalo.")

    for i in range(iter_max):
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tol or (b - a) / 2 < tol:
            return c, i + 1
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) / 2, iter_max

# Plot da função
def plot_func():
    os.makedirs("4", exist_ok=True)
    x_vals = np.arange(0, 3, 0.01)
    y_vals = f(x_vals)

    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.plot(x_vals, y_vals, label="f(x)")
    plt.grid(True)
    plt.title("f(x) = 5sin(x²) - exp(x/10)")
    plt.legend()
    plt.savefig("4/bissecao_atividade3.png", dpi=120, bbox_inches="tight")
    plt.close()

# Isolamento de raízes
def encontrar_intervalos():
    intervalos = []
    x_vals = np.arange(0, 3, 0.1)
    for i in range(len(x_vals) - 1):
        a, b = x_vals[i], x_vals[i + 1]
        if f(a) * f(b) < 0:
            intervalos.append((a, b))
        if len(intervalos) == 3:
            break
    return intervalos

# Função principal
def main():
    print("-- Atividade 3 --")
    plot_func()
    intervalos = encontrar_intervalos()

    for idx, (a, b) in enumerate(intervalos, start=1):
        raiz, it = bissecao(f, a, b, 1e-5)
        print(f"Raiz {idx}: Intervalo ({a:.1f}, {b:.1f}) → x ≈ {raiz:.5f} , iterações = {it}")

# Execução
if __name__ == "__main__":
    main()
