# faça um programa que leia três números e mostre o maior e o menor deles

from lzma import MODE_NORMAL


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
maior = a
if b>c and c>a:
  maior = b
if c>b and b>a:
  maior = c
print (f'O maior é {maior}.')
menor = a
if b<c and c<a:
  menor = b
if c<b and b<a:
  menor = c
print (f'O maior é {menor}.')