import numpy as np
from scipy.integrate import quad
from algoritmos import medio, trapezio, simpson, integral

def atividade1():
    print("-- Atividade 1 --")
    a = 0
    b = 1

    funcoes = [
        ("e^(-x)", lambda x: np.exp(-x)),
        ("x^2", lambda x: x**2),
        ("x^3", lambda x: x**3),
        ("x * e^(-x^2)", lambda x: x * np.exp(-x**2)),
        ("1 / (x^2 + 1)", lambda x: 1 / (x**2 + 1)),
        ("x / (x^2 + 1)", lambda x: x / (x**2 + 1)),
    ]

    for nome, f in funcoes:
        print(f"\nf(x) = {nome}")
        print(f"Ponto médio = {integral(medio, f, a, b):.8f}")
        print(f"Trapézio    = {integral(trapezio, f, a, b):.8f}")
        print(f"Simpson     = {integral(simpson, f, a, b):.8f}")
        r, _ = quad(f, a, b)
        print(f"SciPy       = {r:.8f}")

def atividade2():
    print("\n-- Atividade 2 --")
    def f(x):
        return np.exp(4 - x**2)

    a = 2
    b = 5

    for n in [3, 5, 7, 9]:
        print(f"\nn = {n}")
        x = np.linspace(a, b, n + 1)
        ponto_medio = sum(medio(f, x[i], x[i+1]) for i in range(n))
        trapezios = sum(trapezio(f, x[i], x[i+1]) for i in range(n))
        simpsons = sum(simpson(f, x[i], x[i+1]) for i in range(n))

        print(f"Ponto médio = {ponto_medio:.7f}")
        print(f"Trapézios   = {trapezios:.7f}")
        print(f"Simpson     = {simpsons:.7f}")

def main():
    atividade1()
    atividade2()

if __name__ == "__main__":
    main()
