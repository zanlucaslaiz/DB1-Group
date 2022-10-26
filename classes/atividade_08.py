# Criar uma classe Musica, que deverá receber como parâmetro de criação uma lista de string com as estrofes de uma música. 
# Esta classe deverá conter um método chamado cante_para_mim que imprima todas as estrofes, uma em cada linha. 
# Para executar, instancie a classe e execute o método

class Musica:
    def __init__(self, titulo, compositor, musica:list):
        self.titulo = titulo
        self.compositor = compositor
        self.musica = musica

    def cante_para_mim(self):
        print ('\nTítulo: '+self.titulo)
        print ('\nCompositor: '+self.compositor+'\n')
        print ('\n\n'.join(self.musica)+'\n')


