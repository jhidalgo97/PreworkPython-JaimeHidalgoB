'''
Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
'''
def elementos_no_comunes(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    elementos_no_comunes = list(conjunto1.symmetric_difference(conjunto2))
    
    return elementos_no_comunes

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
resultado = elementos_no_comunes(lista1, lista2)
print("Elementos no comunes entre las listas:")
print(resultado)
