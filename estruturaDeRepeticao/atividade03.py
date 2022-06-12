# faça um programa que peça as 4 notas bimestrais e mostre a media.

soma = cont = 0
for c in range(1,5):
  n = float(input(f'Digite a {c}ª nota:'))
  cont += 1
  soma += n
media = soma / 4  
print(f'Sua média é {media}.')
