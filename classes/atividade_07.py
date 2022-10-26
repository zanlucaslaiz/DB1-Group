# Criar uma classe Triangulo, que receba no seu construtor 3 medidas de ângulos. 
# Criar um método check_angulo que valide as informações dos 3 ângulos informados na criação da classe. 
# Instanciar a classe Triangulo e imprimir os lados informados e imprimir se o triângulo é um triângulo ou não. 
# O método check_angulo deverá retornar True se a soma dos valores for igual a 180 e False em qualquer outra possibilidade;

class Triangulo:
    def __init__(self, ang1, ang2, ang3):
        self.ang1 = ang1
        self.ang2 = ang2
        self.ang3 = ang3
    
    def check_angulo(self):
        soma = self.ang1 + self.ang2 + self.ang3

        if soma == 180:
            True
        else:
            False

    def __str__(self):
        if self.check_angulo():
            return 'É um Triangulo'
        else:
            return 'Não é um triangulo.'

