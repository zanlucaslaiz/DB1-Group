# Escreva um programa que execute uma função que encontre o maior número de uma lista passada por parâmetro.

def maior(list):
  return max(list)
   

num = []

while True:
  x = (int(input('Digite um numero[999 para parar]: ')))
  if x != 999:
      num.append(x)
  elif x == 999:
    break

print (f'O maior número foi {maior(num)}.')


