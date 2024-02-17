'''Ejercicio: Define una función que tome un número y retorne su factorial.
'''
def fact(n):
  if n<0:
    return "Error, el número introducido es negativo"
  elif n==1:
    return 1
  elif n==0:
    return 1
  for i in range (1,n):
    n=n*i
  return n
a=int(input("Introduzca valor para calcular su factorial  "))
print ("El resultado es",(fact(a)))
