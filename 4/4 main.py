  # Atividade 4
import numpy as np
import matplotlib.pyplot as plt

from algoritmos import bissecao




# Função da Atividade4
def f4(x, V, R):
    IR = 1e-12  # corrente de saturação (A)
    T = 300.0  # temperatura (K)
    k = 1.38064852e-23  # constante de Boltzmann (J/K)
    q = 1.60217662e-19  # carga do elétron (C)
    vt = k * T / q  # tensão térmica (V)
    return R * IR * (np.exp(x / vt) - 1) + x - V

def plot(f, xi, xf, d=0.1, num_img=1):
    # Intervalo para plotar
    x_vals = np.arange(xi, xf, d)
    y_vals = f(x_vals)

    plt.axhline(0, color="black", linewidth=1)  # eixo x
    plt.axvline(0, color="black", linewidth=1)  # eixo y
    plt.plot(x_vals, y_vals)
    plt.grid(True)
    plt.title("Visualização da função f(x)")

    # Salvar gráfico como imagem
    plt.savefig(f"4/bissecao_{num_img}.png", dpi=120, bbox_inches="tight")
    plt.close()


def main():
    # Atividade 4
    print("-- Atividade 4 --")
    f4_vr = lambda x: f4(x, 30, 1e3)
    plot(f4_vr, 0, 1, num_img=4)
    VRs = [
        (30, 1e3, 0, 1),
        (3, 1e3, 0, 1),
        (3, 1e4, 0, 1),
        (0.3, 1e3, 0, 0.5),
        (-0.3, 1e3, -1, 0),
        (-30, 1e3, -40, 0),
        (-30, 1e4, -40, 0),
    ]
    for V, R, a, b in VRs:
        try:
            f4_vrs = lambda x: f4(x, V, R)
            r, i = bissecao(f4_vrs, a, b, 1e-8)
            print(f"V={V} V, R={R/1e3:.0f}kΩ --> vd = {r:.3f} V")
        except ValueError as error:
            print(f"V={V} V, R={R/1e3:.0f}kΩ --> {error}")
if __name__ == "__main__":
    main()

     
"""
toda ves que for rodar o programa tem que chamar esse comando para ativar o ambiente virtual
Biblioteca: source .venv/bin/activate
"""
