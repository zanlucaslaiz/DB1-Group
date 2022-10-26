# Criar uma classe que representará uma aeronave militar com o nome JatoMilitar1Lugar. 
# O método construtor deverá receber duas informações iniciais: o modelo e a base onde a aeronave está; 
# Crie um método chamado designar_piloto, que deverá receber o nome do piloto como parâmetro.


class JatoMilitar1Lugar:
    def __init__(self, modelo, baseOrig):
        self.modelo = modelo
        self.baseOrig = baseOrig
        self._historico = [self.base]
        self._designa = False
    
    def designar_piloto(self, piloto):
        self.piloto = piloto
        self._designa = True
    
   