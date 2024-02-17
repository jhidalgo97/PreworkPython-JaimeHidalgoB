'''Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
'''
def invertir_palabras(cadena):
    palabras = cadena.split()  
    palabras_invertidas = palabras[::-1]  
    cadena_invertida = ' '.join(palabras_invertidas)  
    return cadena_invertida


cadena_original = "Hola Mundo Buenos dias"
cadena_invertida = invertir_palabras(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)
