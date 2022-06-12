# faça um programa que leia três números e mostre o maior deles.

maior = 0
cont = 0
for c in range(1,4):
  n = int(input(f'Digite o {c}º número: '))
  cont += 1
  if n > maior:
    maior = n
  else:
    pass  
print(f'O maior é {maior}.')