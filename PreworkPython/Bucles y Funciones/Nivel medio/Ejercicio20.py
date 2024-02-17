'''
Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
'''
def lista_inversa(lista):
    lista_invertida = lista[::-1]
    return lista_invertida


lista_original = [1, 2, 3, 4, 5]
lista_invertida = lista_inversa(lista_original)
print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)
