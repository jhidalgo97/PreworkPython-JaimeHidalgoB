'''
Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.
'''
def divisores(numero):
    lista_divisores = []
    for i in range(1, numero +1):
        if numero % i == 0:
            lista_divisores.append(i)
    return lista_divisores

numero = 15
print("Los divisores de", numero, "son:", divisores(numero))
