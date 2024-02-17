'''Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
'''
def suma_lista(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

numeros = [1, 2, 3, 4, 5]
resultado = suma_lista(numeros)
print("La suma de los números en la lista es:", resultado)
