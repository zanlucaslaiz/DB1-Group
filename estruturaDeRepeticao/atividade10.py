# faça um programa que peça os 3 lados de um triangulo.

print ('Digite os três segmentos do triangulo.')
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
  print ('Esses segmentos formam um triangulo.')
else:
  print ('Esses segmentos não formam um triangulo.')
