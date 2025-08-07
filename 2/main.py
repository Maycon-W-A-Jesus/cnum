#Atividade 01
def is_perfect(n: int) -> bool:
    if n < 1:
        return False

    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i

    return sum_divisors == n


def main():
    assert is_perfect(6) == True
    assert is_perfect(7) == False
    assert is_perfect(-1) == False


if __name__ == "__main__":
    main()

    #Atividade 02
    def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("O número deve ser não negativo.")

    result = 1
    i = n
    while i > 1:
        result *= i
        i -= 1

    return result
    def main():
    assert is_perfect(6) == True
    assert is_perfect(7) == False
    assert is_perfect(-1) == False
    assert factorial(5) == 120
    assert factorial(0) == 1
    try:
        factorial(-1)
    except ValueError as error:
        assert str(error) == "O número deve ser não negativo."
        
        #Atividade 03
        def is_prime(n: int) -> bool:
    ...
    assert is_prime(7) == True
    assert is_prime(10) == False

    #Atividade 04
    def sum_of_digits(n: int) -> int:
    ...
    assert sum_of_digits(123) == 6
    try:
        sum_of_digits(-1)
    except ValueError as error:
        assert str(error) == "O número deve ser não negativo."
        #Atividade 05
