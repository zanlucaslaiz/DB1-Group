# faça um programa que leia três números e mostre o maior e o menor deles

maior = menor = cont = 0
for c in range(1,4):
  n = int(input(f'Digite o {c}º número: '))
  cont += 1
  if n > maior:
    maior = n
  else:
    pass
  if n < menor or menor == 0:
    menor = n
  else:
    pass
print(f'O maior número digitado foi {maior} e o menor foi {menor}.')
