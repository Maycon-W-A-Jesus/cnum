# Atividade 04

import numpy as np
from algoritmos import pontofixo, newton_raphson, secante

# Função 1
f1 = lambda x: np.exp(x) - x - 2
g1 = lambda x: np.exp(x) - 2

# Função 2
f2 = lambda x: np.cos(x) - x**2
g2 = lambda x: x + (np.cos(x) - x**2) / (np.sin(x) + 2*x)

# Função 3
f3 = lambda x: np.exp(-x**2) - 2*x
g3 = lambda x: 0.5 * np.exp(-x**2)

def resolver(nome, f, g, x0, x1=None, df=None):
    print(f"\n-- {nome} --")
    r1 = pontofixo(x0, g)
    print(f"raiz ponto fixo = {r1:.8f}")
    r2 = newton_raphson(x0, f, df=df)
    print(f"raiz newton-raphson = {r2:.8f}")
    if x1 is not None:
        r3 = secante(x0, x1, f)
        print(f"raiz secante = {r3:.8f}")

def main():
    resolver("Função 1", f1, g1, x0=-1.8, x1=-1.7, df=lambda x: np.exp(x) - 1)
    resolver("Função 2", f2, g2, x0=0.5, x1=1.0, df=lambda x: -np.sin(x) - 2*x)
    resolver("Função 3", f3, g3, x0=0.5, x1=0.6, df=lambda x: -2*x*np.exp(-x**2) - 2)

if __name__ == "__main__":
    main()
