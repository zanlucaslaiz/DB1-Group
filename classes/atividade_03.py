# Escreva uma classe em Python que leia dois números e implemente uma exponenciação.

class Exponencial:
    def elevacao(num1=1, num2=1):
        resposta = num1 ** num2
        return resposta
        

num1 = int(input('numero:'))
num2 = int(input('numero: '))
print(Exponencial.elevacao(num1, num2))