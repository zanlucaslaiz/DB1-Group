# faça um programa que peça dois números e imprima o maior deles.

n1 = 0
for c in range(1,3):
  n = int(input(f'Digite o {c}º número: '))
  n1 += 1
  if n > n1:
    maior = n
  elif n < n1:
    maior = n1
print(f'O maior número é {maior}:')

