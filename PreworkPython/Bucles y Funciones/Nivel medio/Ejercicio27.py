'''
Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.
'''
def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

lista_con_duplicados = [1, 2, 3, 4, 2, 3, 5]
lista_sin_duplicados = eliminar_duplicados(lista_con_duplicados)
print("Lista original:", lista_con_duplicados)
print("Lista sin duplicados:", lista_sin_duplicados)
