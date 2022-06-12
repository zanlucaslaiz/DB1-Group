# faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

maisBarato = cont = 0
for c in range(1,4):
  produto = float(input(f'Informe o preço do {c}º produto: '))
  cont += 1
  if produto < maisBarato or maisBarato == 0:
    maisBarato = produto
  else:
    pass
print (f'Você deve comprar o {maisBarato}.')