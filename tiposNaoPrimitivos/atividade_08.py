# escreva um programa que concatene os dicionários abaixo e crie um novo. Exemplo dicionário(Dict):
# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# Resultado esperado: {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}***

musica = {'nome da musica': 'If You Want Love'}
cantor = {'nome do cantor':'Nathan John Feuerstein'}
tempo = {'min': 3, 'seg': 24}
juncao_dicio = {**musica, **cantor, **tempo}
print(juncao_dicio)