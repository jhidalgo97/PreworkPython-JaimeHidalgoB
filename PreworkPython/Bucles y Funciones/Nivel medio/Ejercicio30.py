'''Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
'''
def cadena_mas_larga(lista_cadenas):
    """
    Esta función encuentra y retorna la cadena más larga en una lista de cadenas.
    """
    if not lista_cadenas:
        return None

    cadena_mas_larga = lista_cadenas[0]  
    for cadena in lista_cadenas:
        if len(cadena) > len(cadena_mas_larga):
            cadena_mas_larga = cadena

    return cadena_mas_larga


cadenas = ["Hola", "Hola buenos dias", "Hola buenos dias, que tal"]
cadena_larga = cadena_mas_larga(cadenas)
print("La cadena más larga en la lista es:", cadena_larga)
