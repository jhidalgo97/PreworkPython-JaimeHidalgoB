'''
Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números
'''
def suma_acumulada(lista):
    suma = 0
    suma_acumulada = []
    for numero in lista:
        suma += numero
        suma_acumulada.append(suma)
    return suma_acumulada

numeros = [1, 2, 3, 4, 5]
resultado = suma_acumulada(numeros)
print("Suma acumulada de los números:", resultado)
