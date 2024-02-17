'''
Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
'''
def contar_apariciones(cadena):
    cadena=cadena.lower()
    conteo_caracteres = {}
    for caracter in cadena:
        if caracter in conteo_caracteres:
            conteo_caracteres[caracter] += 1
        else:
            conteo_caracteres[caracter] = 1

    return conteo_caracteres

cadena = "Hola buenos dias hola"
resultado = contar_apariciones(cadena)
print("Conteo de apariciones de cada caracter en la cadena:")
print(resultado)
