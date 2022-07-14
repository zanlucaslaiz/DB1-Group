# Escreva um programa que execute uma função que multiplique todos os números de uma lista passada por parâmetro.

from math import prod

def multLista(list):
  print (f'A multiplicação da lista {prod(list)}')


numero = [8, 5, 4, 1, 5, 8]
multLista(numero)
