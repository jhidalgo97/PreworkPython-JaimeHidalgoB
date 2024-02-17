'''
Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
'''
def contar_digitos_y_letras(cadena):
    contador_digitos = 0
    contador_letras = 0
    for caracter in cadena:
        if caracter.isdigit():
            contador_digitos += 1
        elif caracter.isalpha():
            contador_letras += 1
    
    return contador_digitos, contador_letras

cadena = "Hoy es 17 de Febrero de 2024"
digitos, letras = contar_digitos_y_letras(cadena)
print("Número de dígitos:", digitos)
print("Número de letras:", letras)
