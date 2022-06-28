# Escreva um programa que conte o número de caracteres de uma string (exemplo: ‘google.com” Resultado esperado: {‘o’:3,’g’:2,’.’:1,’e’:1,’l’:1,’m’:1,’c’:1})
from collections import Counter

palavras = input('Digite uma palavra: ').upper()

contador = dict(Counter(palavras))
print(contador)
