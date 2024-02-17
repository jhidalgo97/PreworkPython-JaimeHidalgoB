'''
Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
'''
def ordenar_ascendente(lista):
    return sorted(lista)

mi_lista = [1,3,4,5,6,2,9,8]
lista_ordenada = ordenar_ascendente(mi_lista)
print("Lista original:", mi_lista)
print("Lista ordenada en orden ascendente:", lista_ordenada)
