# Escreva um programa que execute uma função que conte o número de letras maiúsculas e minúsculas de um texto e que ao final, chame outra função para imprimir o resultado.

def contagem(string):
  mai = 0
  min = 0
  for l in string:
    if l.isupper():
      mai +=1
    elif l.islower():
      min += 1
  mostraTotal(mai, min)
  return mai, min


def mostraTotal(mai,min):
  print (f'A frase tem {mai} letras maiusculas.')
  print (f'A frase tem {min} letras minusculas.')


frase = str(input('Digite uma frase: '))
contagem(frase)
