# Atividade 01 14/08/2025

import math
import sys
def exp_series(x, atol=0.0):
    """ Aproxima e^x pela série de Maclaurin com critério de parada numérico. """
    eps = sys.float_info.epsilon
    s = 1.0
    term = 1.0
    n = 0
    tol_abs = max(atol, eps)

    while True:
        n += 1
        term *= x / n
        s += term
        if abs(term) < eps * abs(s) or abs(term) < tol_abs:
            break
        if n > 10_000:
            break
    return s, n, term
"""
# Demonstração
def main():
    for val in [1.0, 5.0, -2.0]:
        approx, nterms, last = exp_series(val)
        print(f"x={val:+g} -> e^x ≈ {approx:.16g} (math.exp={math.exp(val):.16g}, termos={nterms})")

if __name__ == "__main__":
    main()
"""
    # Atividade 02  

def exp_limit(x, atol=1e-12, max_iter=1_000_000):
    """
    Aproxima e^x usando a fórmula do limite:
        e^x ≈ (1 + x/n)^n com n → ∞

    Parâmetros:
        x (float): valor para o qual calcular e^x
        atol (float): tolerância absoluta para critério de parada
        max_iter (int): número máximo de iterações

    Retorna:
        approx (float): valor aproximado de e^x
        n (int): valor de n usado
        delta (float): diferença entre aproximações consecutivas
    """
    n = 1
    prev = 0.0

    while n <= max_iter:
        approx = (1 + x / n) ** n
        delta = abs(approx - prev)

        if delta < atol:
            break

        prev = approx
        n *= 2  # Crescimento exponencial para acelerar convergência

    return approx, n, delta
def main():
# Demonstração
    print("Exemplo de uso da função atividade1:")

    for val in [1.0, 5.0, -2.0]:
        approx, nterms, last = exp_series(val)
        print(f"x={val:+g} -> e^x ≈ {approx:.16g} (math.exp={math.exp(val):.16g}, termos={nterms})")
    
    print("\nExemplo de uso da função atividade2:")   
    for x in [1.0, 5.0, -2.0]:
        resultado, n_final, delta = exp_limit(x)
        print(f"x = {x:+.1f} → e^x ≈ {resultado:.16g} (math.exp = {math.exp(x):.16g}, n = {n_final})")

    for val in [10.0, -20.0]:
    y, k, n = exp_series_scaling(val, theta=1.0)
    print(f"x={val:+g} -> e^x ≈ {y:.6e} (math.exp={math.exp(val):.6e})  [k={k}, termos série(m)={n}]")    

if __name__ == "__main__":
    main()

  


