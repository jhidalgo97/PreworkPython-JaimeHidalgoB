'''
Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

cadena = "Radar"
print("¿La cadena es un palíndromo?", es_palindromo(cadena))
