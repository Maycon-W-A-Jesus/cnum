import numpy as np

def montar_sistema_reduzido(R1, R2, R3, R4, R5, R6, R7, R8, V1):
    """
    Monta o sistema reduzido de 4 equações para as tensões V2, V3, V4, V5.
    """
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

    return A, B

def resolver_sistema(A, B):
    """
    Resolve o sistema linear Ax = B.
    """
    X = np.linalg.solve(A, B)
    return np.round(X, 4)

def exibir_resultados(V1, VA, VB):
    """
    Exibe os resultados em formato de tabela.
    """
    print("\n Tabela de Soluções (4 algarismos significativos):")
    print(f"{'Caso':<6} {'V1':>6} {'V2':>8} {'V3':>8} {'V4':>8} {'V5':>8}")
    print(f"{'A':<6} {V1:>6} {VA[0]:>8.4f} {VA[1]:>8.4f} {VA[2]:>8.4f} {VA[3]:>8.4f}")
    print(f"{'B':<6} {V1:>6} {VB[0]:>8.4f} {VB[1]:>8.4f} {VB[2]:>8.4f} {VB[3]:>8.4f}")

def main():
    V1 = 127

    # Caso A: R5 = 100, R8 = 50
    A_a, B_a = montar_sistema_reduzido(2, 2, 2, 2, 100, 100, 100, 50, V1)
    VA = resolver_sistema(A_a, B_a)

    # Caso B: R5 = 50, R8 = 100
    A_b, B_b = montar_sistema_reduzido(2, 2, 2, 2, 50, 100, 100, 100, V1)
    VB = resolver_sistema(A_b, B_b)

    # Exibir resultados
    exibir_resultados(V1, VA, VB)

if __name__ == "__main__":
    main()
