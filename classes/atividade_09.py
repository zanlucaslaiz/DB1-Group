# Criar uma classe chamada Ponto3D que herde de Object. 
# Na classe Ponto3D, crie um construtor que receba 3 numeros, e armezene-os em 3 variáveis. 
# Crie uma forma para que ao exibir o conteúdo da instancia, a informação apresenta seja: (<num1>; <num2>,<num3>)
# Uso:
# ponto = Ponto3D(1, 2, 3)
# Print(ponto) => (1, 2, 3)

class Ponto(object):
    num1 = []
    num2 = []
    num3 = []

class Ponto3D:
    def numeros(n1, n2, n3):
        Ponto.num1.append(n1)
        Ponto.num2.append(n2)
        Ponto.num3.append(n3)
        return Ponto.num1, Ponto.num2, Ponto.num3


ponto = Ponto3D.numeros(1 , 2 , 3)
print (ponto)