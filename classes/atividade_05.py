# Escreva uma classe em Python que receba como arqumentos um id, um nome e a classe de um estudante, 
# sendo que o nome e a classe não são obrigatórios no momento da instanciação da classe. 
# Crie um método que imprima o id do aluno, e se houver nome, imprima o nome, e se houver classe, imprima a classe também.

class Cadastro:
    def __init__(self, id, nome=None, classe=None):
        self.id = id
        self.nome = nome
        self.classe = classe

    def id(self):
        return self.id, self.nome, self.classe

Cadastro('0001', 'Laiz c. Zanlucas', '1°A')