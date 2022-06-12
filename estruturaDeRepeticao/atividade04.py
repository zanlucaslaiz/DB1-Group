# faça um programa que peça 2 números inteiros e um numero real. Calcule e mostre

soma = cont = 0
for c in range(1,4):
  n = float(input(f'Digite o {c}º número: '))
  cont += 1
  soma += n
print (f'O resultado da soma é {soma:.1f}.')