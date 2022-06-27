# escreva um programa que clone ou copie uma lista.

filmes = []
for f in range(1,4):
  filmes.append(str(input('Digite seus 3 favoritos: ')))
a = filmes[:]
b = filmes
print(filmes)
print(a)
print(b)

 