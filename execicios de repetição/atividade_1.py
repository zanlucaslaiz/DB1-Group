# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhados no mês. Calcule e mostre o total de seu salário no referido mês.

sh = float(input('Qual seu sálario por hora? '))
ht = float(input('Quantas horas trabalhou esse mês? '))
sm = sh * ht
print (f'Seu salário esse mês será {sm}.')