import numpy as np
from algoritmos import G, GN, fixed_point

def main():
    print("-- Atividade 4 --")

    def F(x):
        x1, x2, x3, l = x
        # Derivadas parciais de C1, C2, C3
        dC1 = 0.3 + 2e-4 * x1 + 4 * 3.4e-9 * x1**3
        dC2 = 0.25 + 4e-4 * x2 + 3 * 4.3e-7 * x2**2
        dC3 = 0.19 + 1e-3 * x3 + 4 * 1.1e-7 * x3**3
        return np.array([
            dC1 - l,
            dC2 - l,
            dC3 - l,
            x1 + x2 + x3 - 1500
        ], dtype=float)

    def J(x):
        x1, x2, x3, l = x
        return np.array([
            [2e-4 + 12.4e-9 * x1**2, 0.0, 0.0, -1.0],
            [0.0, 4e-4 + 6 * 4.3e-7 * x2, 0.0, -1.0],
            [0.0, 0.0, 1e-3 + 12 * 1.1e-7 * x3**2, -1.0],
            [1.0, 1.0, 1.0, 0.0]
        ], dtype=float)

    # Aproximação inicial
    x0 = np.array([500.0, 500.0, 500.0, 0.1], dtype=float)

    print("Usando Jacobiana analítica:")
    r1 = fixed_point(x0, lambda x: G(x, F, J))
    print(f"x1 ≈ {r1[0]:.5f}, x2 ≈ {r1[1]:.5f}, x3 ≈ {r1[2]:.5f}")

    print("Usando Jacobiana numérica:")
    r2 = fixed_point(x0, lambda x: GN(x, F))
    print(f"x1 ≈ {r2[0]:.5f}, x2 ≈ {r2[1]:.5f}, x3 ≈ {r2[2]:.5f}")

if __name__ == "__main__":
    main()
