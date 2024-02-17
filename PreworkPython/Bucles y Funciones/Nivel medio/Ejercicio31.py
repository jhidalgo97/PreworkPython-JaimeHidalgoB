''' Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
'''
def es_primo(numero):
    
    #Esta función verifica si un número es primo.
    
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def numeros_primos(n):
    
    #Esta función retorna una lista con los n primeros números primos.
    
    lista_primos = []
    numero = 2
    while len(lista_primos) < n:
        if es_primo(numero):
            lista_primos.append(numero)
        numero += 1
    return lista_primos


n = 10
primos = numeros_primos(n)
print(f"Los {n} primeros números primos son:", primos)
