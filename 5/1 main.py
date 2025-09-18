# Atividade 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import approx_fprime

# Função original e função g(x) para ponto fixo
def f1(x):
    return np.e**x - x - 2

def g1(x):
    return np.e**x - 2

# Método de ponto fixo simples
def pontofixo(a, g, TOL=1e-8):
    x = g(a)
    count = 1
    while abs(x - a) > TOL:
        a = x
        x = g(a)
        count += 1
    return x, count

# Método de Newton-Raphson
def newton_raphson(a, f, TOL=1e-8, df=None):
    if df is None:
        def dfn(x):
            return approx_fprime(np.array([x]), lambda v: f(v[0]))[0]
    else:
        dfn = df
    g = lambda x: x - f(x) / dfn(x)
    return pontofixo(a, g, TOL)

# Método da secante
def secante(a, b, f, TOL=1e-8):
    g = lambda a, b: (a * f(b) - b * f(a)) / (f(b) - f(a))
    x = g(a, b)
    count = 1
    while abs(x - b) > TOL:
        a, b = b, x
        x = g(a, b)
        count += 1
    return x, count

# Função para plotar f1(x)
def plot_f1(xi, xf, d=0.01):
    x_vals = np.arange(xi, xf, d)
    y_vals = f1(x_vals)
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.plot(x_vals, y_vals, label="f(x) = e^x - x - 2")
    plt.grid(True)
    plt.title("Função f(x) da Atividade 01")
    plt.legend()
    plt.savefig("atividade01_funcao.png", dpi=120, bbox_inches="tight")
    plt.close()

# Função principal
def main():
    print("-- Atividade 01: Métodos de Ponto Fixo --")
    plot_f1(-2, 2)

    r1, i1 = pontofixo(-1.8, g1)
    print(f"Raiz (Ponto Fixo)            = {r1:.8f}, Iterações = {i1}")

    r2, i2 = newton_raphson(-1.8, f1, df=lambda x: np.e**x - 1)
    print(f"Raiz (Newton-Raphson com df) = {r2:.8f}, Iterações = {i2}")

    r3, i3 = newton_raphson(-1.8, f1)
    print(f"Raiz (Newton-Raphson est.)   = {r3:.8f}, Iterações = {i3}")

    r4, i4 = secante(-1.8, -1.7, f1)
    print(f"Raiz (Secante)               = {r4:.8f}, Iterações = {i4}")

if __name__ == "__main__":
    main()
