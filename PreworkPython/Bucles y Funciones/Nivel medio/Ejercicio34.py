'''Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
'''
def contar_vocales(cadena):
    vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    contador_vocales = 0

    for caracter in cadena:
        if caracter in vocales:

            contador_vocales += 1
    return contador_vocales


cadena = "Hola Mundo"
cantidad_vocales = contar_vocales(cadena)
print("La cantidad de vocales en la cadena es:", cantidad_vocales)
