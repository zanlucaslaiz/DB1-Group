# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

num = int(input('Informe um numero de 0 a 1000: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'O número digitado foi {num} \nUnidade: {u}; \nDezena: {d}; \nCentena: {c}; \nMilhar: {m}.')