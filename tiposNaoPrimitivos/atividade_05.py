# escreva um programa que conte quantas string tenham tamanho maior que 2 e o primeiro e ultimo caracteres sejam iguais. (Exemplo de lista: [‘abc’,’xyz’,’aba’,’1221’] resultado esperado 2)

palavras = ['AMA', 'LAIZ', 'LEAL', 'ARARA', 'LUZ','1991']
contador = 0
for i in range(0,6):
  if len(palavras[i]) > 2 and palavras[i][0] == palavras[i][-1]:
    contador += 1

print(contador)
