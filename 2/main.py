# Atividade 01:
def is_perfect(n: int) -> bool:
    if n < 1:
        return False

    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i

    return sum_divisors == n


# Atividade 02:
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("O número deve ser não negativo.")

    result = 1
    i = n
    while i > 1:
        result *= i
        i -= 1

    return result

# Atividade 03:
def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# Atividade 04:
def sum_of_digits(n: int) -> int:
    if n < 0:
        raise ValueError("O número deve ser não negativo.")

    return sum(int(digit) for digit in str(n))

def main():
   
    #Atividade 05
    
    #Definindo as matrizes
    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    B = np.array([[11, 12, 13],
                  [14, 15, 16],
                  [17, 18, 19]])

    # Produto matricial
    C = A @ B

    # Exibindo os resultados
    print("Resultado do produto matricula:")
    print(C)
    print("\nFormato da matriz (shape):", C.shape)  # (linhas, colunas)
    print("Quantidade total de elementos (size):", C.size)
    print("Quantidade de linhas (len):", len(C))

main()  

#Atividade 06
#pip install matplotlib
...
import matplotlib.pyplot as plt
...

def plot(n: int) -> None:
    x = np.linspace(-np.pi, np.pi, n)   # n valores entre -pi e pi
    y_sen = np.sin(x)                   # array senos dos valores de x
    y_cos = np.cos(x)                   # array cossenos dos valores de x

    plt.plot(x, y_sen, label='seno')
    plt.plot(x, y_cos, label='cosseno')
    plt.xlim(-np.pi, np.pi)

    plt.xlabel('Ângulo [rad]')
    plt.ylabel('Função trigonométrica(x)')
    plt.grid(True)
    plt.legend()
    plt.savefig("plot.png")  # Salva como imagem no ambiente

    print(f'x =\n{x}')
    print(f'y_sen =\n{y_sen}')
    print(f'y_cos =\n{y_cos}')

...

def main():
