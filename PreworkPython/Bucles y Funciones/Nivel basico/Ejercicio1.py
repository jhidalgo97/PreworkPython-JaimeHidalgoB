'''1. Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.
'''
def es_par(numero):
  return numero % 2 == 0 
num = int(input("Ingresa un número: ")) 
if es_par(num):
  print("Es un número par.")
else:
  print("Es un número impar.")