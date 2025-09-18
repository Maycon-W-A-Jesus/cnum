import numpy as np
from scipy.optimize import approx_fprime
import matplotlib.pyplot as plt

# Função 1
f1 = lambda x: np.e**x - x - 2
g1 = lambda x: np.e**x - 2
df1 = lambda x: np.e**x - 1

# Função 2
f2 = lambda x: np.cos(x) - x**2
g2 = lambda x: x + (np.cos(x) - x**2)/(np.sin(x) + 2*x)
df2 = lambda x: -np.sin(x) - 2*x

# Função 3
f3 = lambda x: np.exp(-x**2) - 2*x
g3 = lambda x: 0.5 * np.exp(-x**2)
df3 = lambda x: -2*x*np.exp(-x**2) - 2

# Método do ponto fixo
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

# Função para plotar f(x)
def plot_fx(f, xi, xf, nome, raiz=None):
    x_vals = np.linspace(xi, xf, 400)
    y_vals = f(x_vals)
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.plot(x_vals, y_vals, label=f"{nome}(x)", color="blue")
    if raiz:
        plt.plot(raiz, f(raiz), 'ro', label=f"Raiz ≈ {raiz:.7f}")
    plt.grid(True)
    plt.title(f"Função {nome}(x) da Atividade 04")
    plt.legend()
    plt.savefig(f"atividade04_funcao_{nome}.png", dpi=120, bbox_inches="tight")
    plt.close()

# Função principal
def main():
    print("-- Atividade 04: Métodos Numéricos --")

    # Função 1
    r1_pf, i1_pf = pontofixo(-1.8, g1)
    r1_nr, i1_nr = newton_raphson(-1.8, f1, df=df1)
    r1_sc, i1_sc = secante(-1.8, -1.7, f1)
    print(f"[f1] Ponto Fixo: {r1_pf:.8f} ({i1_pf} iterações)")
    print(f"[f1] Newton-Raphson: {r1_nr:.8f} ({i1_nr} iterações)")
    print(f"[f1] Secante: {r1_sc:.8f} ({i1_sc} iterações)")
    plot_fx(f1, -2, 2, "f1", r1_pf)

    # Função 2
    r2_pf, i2_pf = pontofixo(0.5, g2)
    r2_nr, i2_nr = newton_raphson(0.5, f2, df=df2)
    r2_sc, i2_sc = secante(0.4, 0.6, f2)
    print(f"[f2] Ponto Fixo: {r2_pf:.8f} ({i2_pf} iterações)")
    print(f"[f2] Newton-Raphson: {r2_nr:.8f} ({i2_nr} iterações)")
    print(f"[f2] Secante: {r2_sc:.8f} ({i2_sc} iterações)")
    plot_fx(f2, 0, 1.5, "f2", r2_pf)

    # Função 3
    r3_pf, i3_pf = pontofixo(0.3, g3)
    r3_nr, i3_nr = newton_raphson(0.3, f3, df=df3)
    r3_sc, i3_sc = secante(0.2, 0.5, f3)
    print(f"[f3] Ponto Fixo: {r3_pf:.8f} ({i3_pf} iterações)")
    print(f"[f3] Newton-Raphson: {r3_nr:.8f} ({i3_nr} iterações)")
    print(f"[f3] Secante: {r3_sc:.8f} ({i3_sc} iterações)")
    plot_fx(f3, 0, 1, "f3", r3_pf)

if __name__ == "__main__":
    main()
