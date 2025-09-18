# Atividade 02
import numpy as np

# Função f(x) = cos(x) - x²
def f2(x):
    return np.cos(x) - x**2

# Função iterativa g(x) conforme fórmula fornecida
def g2(x):
    return x + (np.cos(x) - x**2) / (np.sin(x) + 2 * x)

# Método de ponto fixo com tolerância no quinto dígito significativo
def pontofixo(x0, g, TOL=1e-5, max_iter=100):
    x = g(x0)
    count = 1
    while abs(x - x0) > TOL and count < max_iter:
        x0 = x
        x = g(x0)
        count += 1
    return x, count

# Função principal
def main():
    print("-- Atividade 02: Método do Ponto Fixo --")
    x0 = 1.0  # Valor inicial
    raiz, iteracoes = pontofixo(x0, g2)
    print(f"Raiz aproximada = {raiz:.5f}")
    print(f"Iterações       = {iteracoes}")

if __name__ == "__main__":
    main()
