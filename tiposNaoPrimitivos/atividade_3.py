# Escreva um programa que retorne o maior e o menor número de uma lista.

num = []

while True:
  x = (int(input('Digite um numero[000 para parar]: ')))
  if x != 000:
      num.append(x)
  elif x == 000:
    break

print(f'Os números digitados foram {num}.')
print(f'O maior número foi {max(num)}')
print(f'O menor números foi {min(num)}')