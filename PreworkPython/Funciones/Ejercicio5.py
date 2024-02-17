'''Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
'''
def reversa(cadena):
    return cadena[::-1]

texto = input("Introduce una cadena de texto: ")
texto_reversa = reversa(texto)
print("La cadena en reversa es:", texto_reversa)
