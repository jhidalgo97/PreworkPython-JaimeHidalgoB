'''
Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.
'''
def contar_vocales(cadena):
    vocales = ['a', 'e', 'i', 'o', 'u']
    cadena = cadena.lower()
    contador_vocales = 0
    for caracter in cadena:
        if caracter in vocales:
            contador_vocales += 1
    return contador_vocales


cadena = "Buenos dias compañeros"
print("El número de vocales en la cadena '{}' es: {}".format(cadena, contar_vocales(cadena)))
