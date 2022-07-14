# Escreva um programa que execute uma função que calcule o fatorial de um número passado por parâmetro.

def fatorial(c):
  c = n
  f = 1
  while c > 0:
    print(f'{c}', end='')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
  print(f'{f}')




n = int(input('Informe um número: '))
fatorial(n)