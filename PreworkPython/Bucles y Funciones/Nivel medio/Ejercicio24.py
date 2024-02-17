'''
Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.'''
def tabla_de_multiplicar(numero):
    tabla = {}
    for i in range(1, 11):
        resultado = numero * i
        tabla[i] = resultado
    return tabla


numero = 5
tabla_multiplicar_5 = tabla_de_multiplicar(numero)
print("Tabla de multiplicar del", numero)
print(tabla_multiplicar_5)
