# Escreva um programa que multiplique todos os itens de uma lista.
# entendi que eram para ser multiplicados um termo pelo seguinte então essa é minha solução.

from math import prod

num = []
print('Vamos multiplicar!')
n = int(input('Informe quantos números serão multiplicados: '))

while len(num) < n:
  num.append(int(input('Digite um número: ')))
print(f'O produto é {prod(num)}')

