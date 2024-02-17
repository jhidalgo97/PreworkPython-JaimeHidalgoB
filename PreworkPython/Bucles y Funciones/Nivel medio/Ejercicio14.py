''' Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
'''
def palabras_mas_largas_que_n(lista_palabras, n):
    palabras_largas = []
    for palabra in lista_palabras:
        if len(palabra) > n:
            palabras_largas.append(palabra)
    return palabras_largas


lista_palabras = ["manzana", "coche", "pera", "kiwi", "uva", "naranja","motocicleta"]
n = 4
print("Palabras más largas que", n, ":", palabras_mas_largas_que_n(lista_palabras, n))
