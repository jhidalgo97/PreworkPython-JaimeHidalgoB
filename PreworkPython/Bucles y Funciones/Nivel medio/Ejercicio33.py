'''Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
'''
def ordenar_por_ultimo_elemento(lista_tuplas):

    return sorted(lista_tuplas, key=lambda x: x[-1])


lista_tuplas = [(1, 4), (3, 2), (5, 1)]
lista_ordenada = ordenar_por_ultimo_elemento(lista_tuplas)
print("Lista original:", lista_tuplas)
print("Lista ordenada por último elemento:", lista_ordenada)
