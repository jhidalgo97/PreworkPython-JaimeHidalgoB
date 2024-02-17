'''
 Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.
 '''
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n + 1:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[n]

numero = 10
print("El número Fibonacci en la posición", numero, "es:", fibonacci(numero))
