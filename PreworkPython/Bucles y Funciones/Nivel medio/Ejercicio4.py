'''
Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos
'''
def suma_digitos(numero):
    numero_str = str(numero)
    suma = 0
    for digito in numero_str:
        suma += int(digito)
    return suma

numero = 11224
print("La suma de los dígitos de", numero, "es:", suma_digitos(numero))
