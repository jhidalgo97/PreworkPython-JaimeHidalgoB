'''Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci.
'''
def fibonacci(numeros):
    fib_sequence = []
    a, b = 0, 1
    for numero in range(numeros):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def imprimir_fibonacci(numeros):
    fib_sequence = fibonacci(numeros)
    print("Los primeros", numeros, "números de la serie de Fibonacci son:")
    for num in fib_sequence:
        print(num,end=" ")

numeros = 10  
imprimir_fibonacci(numeros)
