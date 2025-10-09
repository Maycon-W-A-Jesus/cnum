# Atividade 2

import numpy as np
from algoritmos import G, GN, fixed_point

def main():
    print("Atividade 2")

    def F(x):
        x1, x2, x3 = x
        return np.array([
            6 * x1 - 2 * x2 + np.exp(x3) - 2,
            np.sin(x1) - x2 + x3,
            np.sin(x1) + 2 * x2 + 3 * x3 - 1
        ], dtype=float)

    def J(x):
        x1, x2, x3 = x
        return np.array([
            [6.0, -2.0, np.exp(x3)],
            [np.cos(x1), -1.0, 1.0],
            [np.cos(x1), 2.0, 3.0]
        ], dtype=float)

    x0 = np.array([0.0, 0.0, 0.0], dtype=float)

    print("Usando Jacobiana analítica:")
    r1 = fixed_point(x0, lambda x: G(x, F, J))
    print(r1)

    print("Usando Jacobiana numérica:")
    r2 = fixed_point(x0, lambda x: GN(x, F))
    print(r2)

if __name__ == "__main__":
    main()
