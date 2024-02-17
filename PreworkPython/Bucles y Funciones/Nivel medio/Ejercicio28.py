'''
Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.
'''
def suma_cuadrados_pares(numero):
    suma = 0
    for i in range(1, numero + 1):
        if i % 2 == 0:
            suma += i ** 2
    return suma


numero = 6
resultado = suma_cuadrados_pares(numero)
print("La suma de los cuadrados de los números pares hasta", numero, "es:", resultado)
