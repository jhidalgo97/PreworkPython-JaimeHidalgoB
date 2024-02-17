'''Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
'''
def calcular_promedio(lista_numeros):
    """
    Esta función calcula el promedio de una lista de números.
    """
    if not lista_numeros:
        return 0
    suma_total = sum(lista_numeros)
    cantidad_numeros = len(lista_numeros)
    promedio = suma_total / cantidad_numeros
    return promedio

numeros = [1, 2, 3, 4, 5]
promedio = calcular_promedio(numeros)
print("El promedio de los números en la lista es:", promedio)
