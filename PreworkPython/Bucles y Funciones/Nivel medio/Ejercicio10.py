'''
Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
'''
def interseccion_listas(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    interseccion = set1.intersection(set2)
    interseccion = sorted(list(interseccion))
    return interseccion

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print("La intersección de las listas es:", interseccion_listas(lista1, lista2))
