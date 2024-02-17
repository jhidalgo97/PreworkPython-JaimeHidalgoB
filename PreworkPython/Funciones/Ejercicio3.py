'''
Define una función que tome un número y determine si es primo.
'''
def prim(x):
  if x==1:
    return "No es primo"
  elif x==2:
    return "Es primo"
  else:
    for i in range (2, x):
      if x % i == 0:
        return "No es primo"
    return "Es primo"


a=int(input('Introduzca un número  '))
print(prim(a))
