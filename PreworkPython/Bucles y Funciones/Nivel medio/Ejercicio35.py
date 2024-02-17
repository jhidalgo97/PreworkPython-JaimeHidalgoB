'''
Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.
'''
def es_primo(numero):

    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

numero = 17
resultado = es_primo(numero)
print(f"¿{numero} es primo?: {resultado}")
