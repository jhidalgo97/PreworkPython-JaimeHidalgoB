'''
Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.'''
def numero_mas_grande(lista):
    return max(lista)


numeros = [10, 20, 5, 30, 15, 100, 123, 3.4]
print("El número más grande en la lista es:", numero_mas_grande(numeros))
