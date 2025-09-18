#Atividade 04
import numpy as np

def resolver_circuito_reduzido(R1, R2, R3, R4, R5, R6, R7, R8, V1):
    A = np.array([
        [-1/R1 - 1/R2 - 1/R5, 0, 0, 1/R2],
        [1/R2, -1/R2 - 1/R3 - 1/R6, 1/R3, 0],
        [0, 1/R3, -1/R3 - 1/R4 - 1/R7, 1/R4],
        [0, 0, 1/R4, -1/R4 - 1/R8]
    ], dtype=float)

    B = np.array([
        -V1 / R1,
        0,
        0,
        0
    ], dtype=float)

    X = np.linalg.solve(A, B)
    return np.round(X, 4)

def main():
    print("-- Atividade 4 (Sistema Reduzido) --")

    V1 = 127

    # Caso A
    R1 = R2 = R3 = R4 = 2
    R5 = R6 = R7 = 100
    R8 = 50
    resultado_a = resolver_circuito_reduzido(R1, R2, R3, R4, R5, R6, R7, R8, V1)
    print("\nCaso A (R5=100, R8=50):")
    print(f"V2={resultado_a[0]} V3={resultado_a[1]} V4={resultado_a[2]} V5={resultado_a[3]}")

    # Caso B
    R1 = R2 = R3 = R4 = 2
    R5 = 50
    R6 = R7 = R8 = 100
    resultado_b = resolver_circuito_reduzido(R1, R2, R3, R4, R5, R6, R7, R8, V1)
    print("\nCaso B (R5=50, R8=100):")
    print(f"V2={resultado_b[0]} V3={resultado_b[1]} V4={resultado_b[2]} V5={resultado_b[3]}")

if __name__ == "__main__":
    main()
