'''
Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
'''
def suma_digitos_y_cubo(numero):
    suma_digitos = sum(int(digito) for digito in str(numero))
    resultado = suma_digitos ** 3
    return resultado


numero = 1223
resultado = suma_digitos_y_cubo(numero)
print("El resultado de sumar los dígitos y luego elevar al cubo es:", resultado)

