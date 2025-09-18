  # Atividade 03 15/08/2025
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

def exp_series_scaling(x, theta=1.0):
    if x == 0.0:
        return 1.0, 0, 0.0, 0
    k = max(0, math.ceil(math.log2(abs(x)/theta))) if abs(x) > theta else 0
    m = x / (2**k)

    em, n_terms, _ = exp_series(m)
    y = em
    for _ in range(k):
        y *= y

    return y, k, n_terms

# Demonstração
def main ( ):
    for val in [10.0, -20.0]:
        y, k, n = exp_series_scaling(val, theta=1.0)
        print(f"x={val:+g} -> e^x ≈ {y:.6e} (math.exp={math.exp(val):.6e})  [k={k}, termos série(m)={n}]")
    
if __name__ == "__main__":
    main()

    # Atividade 04 15/08/2025
    import math

# Função que calcula cos(x) com recursão e critério de parada por epsilon
def cos_series(x, epsilon=1e-12):
    term = 1.0  
    sum_ = term
    n = 0

    while abs(term) > epsilon:
        term *= -x**2 / ((2*n + 1)*(2*n + 2))  # Recursão
        sum_ += term
        n += 1

    return sum_, n 

# Gera 200 pontos entre -20 e 20
xs = [-20 + 40 * i / 199 for i in range(200)]

# Calcula erro relativo para cada ponto
errs = [abs(cos_series(x)[0] - math.cos(x)) / abs(math.cos(x)) for x in xs]

# Exibe número de termos necessários para atingir tolerância em alguns pontos
for x in [1, 3, 10]:
    _, n = cos_series(x, epsilon=1e-12)
    print(f"x = {x}: ~{n} termos para atingir tol = 1e-12")
