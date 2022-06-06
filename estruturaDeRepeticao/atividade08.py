# faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input('Digite o valor do primeiro produto: '))
p2 = float(input('Digite o valor do segundo produto: '))
p3 = float(input('Digite o valor do terceiro produto: '))
maisBarato = p1
if p2<p3 and p3<p1:
  maisBarato = p2
if p3<p2 and p2<p1:
  maisBarato = p3
print (f'Você deve comprar o {maisBarato}.')