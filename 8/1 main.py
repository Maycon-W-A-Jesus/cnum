# Atividade 1

# main.py

from algoritmos import bissecao

def atividade1():
    E = 500.125
    K = 272.975

    def f(T):
        return 5.67e-8 * T**4 + 0.4 * (T - K) - E

    T_minima = bissecao(f, 273, 400)
    print("🔹 Atividade 1: Temperatura mínima da placa")
    print(f"T = {T_minima:.17f} K")

if __name__ == "__main__":
    atividade1()
