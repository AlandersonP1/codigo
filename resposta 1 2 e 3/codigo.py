def is_fibonacci(n):
    if n < 0:
        return False


    def is_perfect_square(x):
        s = int(x ** 0.5)
        return s * s == x


    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)



numero = int(input("Digite um número: "))
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
