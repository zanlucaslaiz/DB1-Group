# Escreva um programa que execute uma função que receba um número informado no console como parâmetro e verifique se o número informado é primo ou não. Nota: Número primo é um número natural, maior que 1 e que não tenha outros divisores além do 1 e dele mesmo.

def numeroPrimo(n):
  cont = 0
  for i in range(1, n + 1):
    if n % i == 0:
      cont += 1

  if cont == 2:
    print('Número é primo.')
  else:
    print('Número não é primo.')


print ('Vamos descobrir se uma número é primo.')
n = int(input('Digite um número: '))
numeroPrimo(n)
