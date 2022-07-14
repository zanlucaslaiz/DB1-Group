# Escreva um programa que execute uma função que valide se o número informado é um número perfeito ou não.
# De acordo com a Wikipedia, um número perfeito é um número inteiro, positivo que seja igual à soma de todos os seus divisores positivos excluindo o próprio número. Equivalente a isto, um número perfeito é a metade da soma de todos os seus divisores positivos, incluindo o próprio número.
# Ex:
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 6 = 12 / 2 = 6
# O próximo número perfeito seria 28.
# 1 + 2 + 4 + 7 + 14 = 28


def numeroPerfeito(a):
    soma = 0
    for i in range(1, a):
        if a % i == 0:
           soma += i        
    if soma != a:
          print (f'{a} não é um número perfeito.')
    else:
          print (f'{a} é um número perfeito.')
           
    
n = int(input('Digite um numero: '))
numeroPerfeito(n)