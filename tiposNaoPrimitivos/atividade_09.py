# Escreva um programa que leia chaves e valores, crie um dicionário, e depois, verifique se uma chave informada existe em um dicionário.

print('Lista de filmes.')
filmes = {}
while True:
  item1 = (str(input(f'Digite tipo de filmes[digite 0 para parar]: '))).upper()
  if item1 in '0':
    break
  item2 = (str(input('Nome do filme: '))).upper()
  filmes.update({item1: item2})

print(filmes)
print('-=' * 30)
print('Vamos buscar um filme')

f = str(input('Digite o tipos de filme: ')).upper()

if f in filmes:
  print(f'Esse filme {f} já está na lista de filmes.')
else:
  print('Esse filme não existe na lista de filmes.')

print('Fim da busca.')