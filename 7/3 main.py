import numpy as np
from algoritmos import G, GN, fixed_point

def main():
    print("Atividade 3")

    def F(x):
        x1, x2 = x
        return np.array([
            (x1**2)/8 + ((x2 - 1)**2)/5 - 1,
            np.arctan(x1) + x1 - x2 - x2**3
        ], dtype=float)

    def J(x):
        x1, x2 = x
        return np.array([
            [x1 / 4, (2 * (x2 - 1)) / 5],
            [1 / (1 + x1**2) + 1, -1 - 3 * x2**2]
        ], dtype=float)

    # Pontos
    pontos_iniciais = [
        np.array([-1.2085435, -1.0216674], dtype=float),
        np.array([2.7871115, 1.3807962], dtype=float)
    ]

    for i, x0 in enumerate(pontos_iniciais, start=1):
        print(f"\nPonto inicial {i}: {x0}")
        r1 = fixed_point(x0, lambda x: G(x, F, J))
        print("Usando Jacobiana analítica:", r1)

        r2 = fixed_point(x0, lambda x: GN(x, F))
        print("Usando Jacobiana numérica:", r2)

if __name__ == "__main__":
    main()
