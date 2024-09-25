def fibonacci_sequence(limit):
    fib_sequence = [0, 1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > limit:
            break
        fib_sequence.append(next_fib)
    return fib_sequence

def belongs_to_fibonacci(n):
    fib_sequence = fibonacci_sequence(n)
    return n in fib_sequence

# Defina o número aqui ou descomente a parte de entrada
number = int(input("Digite um número: "))  # Entrada do usuário

if belongs_to_fibonacci(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")
