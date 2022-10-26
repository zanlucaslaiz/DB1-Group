# 4 Escreva uma classe em Python que possua 2 métodos, um chamado adicionar_string e outro chamado inverter_string. 
# O primeiro método deverá receber uma string como parâmetro e armazená-la em um array. 
# O segundo, deverá listar as strings invertidas no seu conteúdo e também, na sua ordem de inclusão.

class Texto:
    def __init__(self, lista) -> None:
        self.lista = lista

    def adicionar(self, string):
        self.string = string
        self.lista.append(self.string)
        
        return self.lista

    def inverter(self):
        invertida = []
        
        for i in range (-1, -1-len(self.lista), -1):
            invertida.append(self.lista[i][::-1])
        
        return invertida

