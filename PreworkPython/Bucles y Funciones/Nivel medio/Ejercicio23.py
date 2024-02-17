'''
Ejercicio: Define una función que encuentre el elemento más común en una lista.
'''
from collections import Counter

def elemento_mas_comun(lista):
    conteo = Counter(lista)
    
    elemento_mas_comun = max(conteo, key=conteo.get)
    frecuencia_maxima = conteo[elemento_mas_comun]
    
    return elemento_mas_comun, frecuencia_maxima

numeros = [1, 2, 3, 4, 2, 2, 3, 3, 3, 3]
elemento, frecuencia = elemento_mas_comun(numeros)
print("Elemento más común:", elemento)
print("Frecuencia:", frecuencia)
