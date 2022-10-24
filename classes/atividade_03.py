# Escreva uma classe em Python que leia dois números e implemente uma exponenciação.

class Exponenciacao:
    def __init__(self, num1) -> None:
        self.num1 = num1
    
    def exponencial(self, num2):
        if isinstance(num2, Exponenciacao):               
            exp = self.num**num2.num
        else:
            exp = self.num**num2

        return exp