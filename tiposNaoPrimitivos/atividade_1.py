# Escreva um programa que some todos os itens de um lista.()
n = []
while True:
  n.append(int(input('Digite um número: ')))
  resp = str(input('Quer continuar?[S/N] ')).upper()[0]
  if resp == 'N':
    break
soma = sum(n)
print(f'A soma da lista {n} é {soma}.')

