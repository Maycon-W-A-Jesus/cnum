import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import os

from algoritimos import( 
    newton, 
    lagrange, 
    polinomial
)

def plot(x, y, num_img=1):
    os.makedirs("9", exist_ok=True)
    x_vals = np.linspace(min(x) - 0.25, max(x) + 0.25, 400)
    yn = np.polyval(newton(x, y), x_vals)
    yl = np.polyval(lagrange(x, y), x_vals)
    yp = np.polyval(polinomial(x, y), x_vals)
    ys = CubicSpline(x, y, bc_type="natural")(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, yn, label="Newton")
    plt.plot(x_vals, yl, label="Lagrange", linestyle="--")
    plt.plot(x_vals, yp, label="Polinomial", linestyle=":")
    plt.plot(x_vals, ys, label="Spline cúbica", linewidth=2)
    plt.scatter(x, y, label="Pontos", zorder=5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Interpolação - Atividade {num_img}")
    plt.legend()
    plt.grid(True, linestyle=":")
    plt.tight_layout()
    plt.savefig(f"9/interpolacao_{num_img}.png", dpi=120)
    plt.close()

def executar_atividade(x, y, xr, num_img):
    yn = np.polyval(newton(x, y), xr)
    yl = np.polyval(lagrange(x, y), xr)
    yp = np.polyval(polinomial(x, y), xr)
    ys = CubicSpline(x, y, bc_type="natural")(xr)

    for xi, n, l, p, s in zip(xr, yn, yl, yp, ys):
        print(f"x = {xi:>4}:  N={n: .6f} | L={l: .6f} | P={p: .6f} | S={s: .6f}")

    plot(x, y, num_img)

def main():
    print("-- Atividade 1 --")
    x1 = np.array([-2.0, 0.0, 1.0, 2.0])
    y1 = np.array([-47.0, -3.0, 4.0, 41.0])
    xr1 = np.array([-1.0, 0.5, 1.5])
    executar_atividade(x1, y1, xr1, 1)

    print("-- Atividade 2 --")
    x2 = np.array([-1.0, 0.5, 1.0, 1.25])
    y2 = np.array([1.25, 0.5, 1.25, 1.8125])
    xr2 = np.array([-0.5, 0.0, 0.25])
    executar_atividade(x2, y2, xr2, 2)

    print("-- Atividade 3 - Questão (a) --")
    x3 = np.array([-50.0, -5.0, 5.0, 75.0])
    y3 = np.array([-300.0, -50.0, 180.0, 350.0])
    xr3 = np.array([0.0])
    executar_atividade(x3, y3, xr3, 3)

    print("-- Atividade 3 - Questão (b) --")
    x4 = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
    y4 = np.array([80.0, -60.0, 40.0, -30.0, 20.0, -10.0, 5.0, -2.5, 1.25, -0.625, 0.3125])
    xr4 = np.array([8.5])
    executar_atividade(x4, y4, xr4, 4)

if __name__ == "__main__":
    main()
