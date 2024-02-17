'''
Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
'''
def segundo_mas_grande(lista):
    lista_ordenada = sorted(lista, reverse=True)
    
    segundo_mas_grande = lista_ordenada[1]
    
    return segundo_mas_grande

numeros = [10, 5, 20, 15, 8]
print("El segundo número más grande es:", segundo_mas_grande(numeros))
