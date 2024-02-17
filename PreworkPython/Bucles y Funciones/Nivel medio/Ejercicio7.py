'''
Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
'''
def contar_letras(cadena):
    mayusculas = 0
    minusculas = 0
    for caracter in cadena:
        if caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1
    return mayusculas, minusculas

cadena = "Buenos días Compañeros"
mayusculas, minusculas = contar_letras(cadena)
print("Cantidad de letras mayúsculas:", mayusculas)
print("Cantidad de letras minúsculas:", minusculas)
