'''
Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
'''
def tienen_miembro_comun(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    if conjunto1.intersection(conjunto2):
        return True
    else:
        return False

lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 7, 8, 9, 10]
print(tienen_miembro_comun(lista1, lista2))

