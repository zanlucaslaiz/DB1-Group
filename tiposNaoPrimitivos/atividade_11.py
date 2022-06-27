# escreva um programa que remova itens duplicados de uma lista.

num = []
n = 0
while True:
  n = (int(input('Digite um numero: ')))
  if n not in num:
    num.append(n)
  else:
    print('Valor já existe!')
  resp = str(input('Quer continuar?[S/N]: '))
  if resp in 'Nn':
    break
num.sort()
print(num)