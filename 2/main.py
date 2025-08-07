# Atividade 01: Verifica se um número é perfeito
def is_perfect(n: int) -> bool:
    if n < 1:
        return False

    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i

    return sum_divisors == n


# Atividade 02: Calcula o fatorial de um número
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("O número deve ser não negativo.")

    result = 1
    i = n
    while i > 1:
        result *= i
        i -= 1

    return result


# Atividade 03: Verifica se um número é primo
def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Atividade 04: Soma os dígitos de um número
def sum_of_digits(n: int) -> int:
    if n < 0:
        raise ValueError("O número deve ser não negativo.")

    return sum(int(digit) for digit in str(n))


# Função principal com testes
def main():
    # Testes da Atividade 01
    assert is_perfect(6) == True
    assert is_perfect(7) == False
    assert is_perfect(-1) == False

    # Testes da Atividade 02
    assert factorial(5) == 120
    assert factorial(0) == 1
    try:
        factorial(-1)
    except ValueError as error:
        assert str(error) == "O número deve ser não negativo."

    # Testes da Atividade 03
    assert is_prime(7) == True
    assert is_prime(10) == False

    # Testes da Atividade 04
    assert sum_of_digits(123) == 6
    try:
        sum_of_digits(-1)
    except ValueError as error:
        assert str(error) == "O número deve ser não negativo."

    print("Todos os testes passaram com sucesso!")


if __name__ == "__main__":
    main()

        #Atividade 05
