# Atividade 1

import numpy as np
from algoritmos import G, GN, fixed_point

def main():
    print("Atividade 1")

    def F(x):
        x1, x2, x3 = x
        return np.array([
            2.0 * x1 - x2 - np.cos(x1),
            -x1 + 2.0 * x2 - x3 - np.cos(x2),
            -x2 + x3 - np.cos(x3)
        ], dtype=float)

    def J(x):
        x1, x2, x3 = x
        return np.array([
            [2.0 + np.sin(x1), -1.0, 0.0],
            [-1.0, 2.0 + np.sin(x2), -1.0],
            [0.0, -1.0, 1.0 + np.sin(x3)]
        ], dtype=float)

    x0 = np.array([1.0, 1.0, 1.0], dtype=float)

    print("Usando Jacobiana analítica:")
    r1 = fixed_point(x0, lambda x: G(x, F, J))
    print(r1)

    print("Usando Jacobiana numérica:")
    r2 = fixed_point(x0, lambda x: GN(x, F))
    print(r2)

if __name__ == "__main__":
    main()

