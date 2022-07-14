# Escreva um programa que execute uma função que some todos os itens de uma lista passada por parâmetro.

def somaLista(list):
  print(f'A soma do itens é {sum(list)}.')

soma = []
while True:
  x = int(input('Digite um número[000 para parar]: '))
  if x != 000:
    soma.append(x)
  elif x == 000:
    break

somaLista(soma)


