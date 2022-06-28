# escreva um programa que ordene em ordem crescente uma lista de tupla informadas, pelo ultimo item da tupla (exemplo de lista: [(2,5),(1,2),(4,4),(2,3),(2,1)] resultado esperado: [(2,1),(1,2),(2,3),(4,4),(2,5)])

lista = [(2,5),(1,2),(4,4),(2,3),(2,1)]

lista.sort(key=lambda x: x[1], reverse=False)
print(lista)