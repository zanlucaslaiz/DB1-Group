# Escreva um programa que execute uma função que retorne o inverso de uma string passada por parâmetro.

def inverso(a):
  return a [: : -1]

texto = str(input('Digite uma frase: ')).strip()
print (inverso(texto))
