'''
Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.
'''
def elementos_unicos(lista):
    # Convertir la lista en un conjunto para eliminar duplicados
    conjunto_elementos = set(lista)
    # Convertir el conjunto de nuevo a lista para preservar el orden original de los elementos
    lista_unicos = list(conjunto_elementos)
    return lista_unicos


lista_original = [1, 2, 3, 4, 5, 3, 6, 7, 9, 8, 1, 2, 3]
print("Lista original:", lista_original)
print("Elementos únicos:", elementos_unicos(lista_original))
