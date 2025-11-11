import numpy as np
from algoritmos import dp, dr, dc

def atividade1():
    print("-- Atividade 1 --")
    h1 = 1e-2
    h2 = 1e-3
    eps = np.finfo(float).eps

    print("\nDerivadas para f(x) = sin(x) em x = 2")
    f = lambda x: np.sin(x)
    print(f"Progressiva: h={h1} → {dp(f, 2, h1):.5f}, h={h2} → {dp(f, 2, h2):.5f}")
    print(f"Regressiva:  h={h1} → {dr(f, 2, h1):.5f}, h={h2} → {dr(f, 2, h2):.5f}")
    print(f"Central:     h={h1} → {dc(f, 2, h1):.5f}, h={h2} → {dc(f, 2, h2):.5f}")
    print(f"Exata: cos(2) = {np.cos(2):.5f}")

    print("\nDerivadas para f(x) = e^(-x) em x = 1")
    f = lambda x: np.exp(-x)
    print(f"Progressiva: h={h1} → {dp(f, 1, h1):.5f}, h={h2} → {dp(f, 1, h2):.5f}")
    print(f"Regressiva:  h={h1} → {dr(f, 1, h1):.5f}, h={h2} → {dr(f, 1, h2):.5f}")
    print(f"Central:     h={h1} → {dc(f, 1, h1):.5f}, h={h2} → {dc(f, 1, h2):.5f}")
    print(f"Exata: -e^(-1) = {-np.exp(-1):.5f}")

def main():
    atividade1()

if __name__ == "__main__":
    main()
