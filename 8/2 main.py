# Atividade 2

from algoritmos import seidel
import numpy as np

if __name__ == "__main__":
    A = np.array([
        [17, -2, -3],
        [-5, 21, -2],
        [-5, -5, 22]
    ], dtype=float)

    B = np.array([500, 200, 300], dtype=float)

    R = seidel(A, B)

    print("Tensões nominais dos reatores")
    print(f"R1 = {R[0]:.6f}")
    print(f"R2 = {R[1]:.6f}")
    print(f"R3 = {R[2]:.6f}")
