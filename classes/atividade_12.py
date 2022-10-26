# Criar uma classe que representará outro tipo de aeronave militar, com o nome JatoMilitar2Lugares. 
# O método construtor deverá receber duas informações: o modelo, e a base onde a aeronave está; 
# Cria um método chamado designar_piloto que deverá contar o nome do piloto. 
# Por regra, o primeiro piloto será considerado o piloto principal e o segundo, o seu copiloto. 
# Depois de informados os dois nomes, não poderá ser inserido mais nenhum nome.
# Criar um método rebasear_aeronave, que receberá como parâmetro o nome da base para onde a aeronave deverá ser enviada. 
# Antes de registrar, é necessário validar se dois pilotos foram designados para a aeronave, e somente se ambos tiverem sido designados, 
# registrar o rebaseamento, com a data e hora da movimentação.
# Sobrescreva o métod __str__ da classe, para imprimir o seguinte conteúdo:
# Jato: <NOME DA AERONAVE>
# Base inicial: <NOME DA BASE DE ORIGEM>
# Piloto: <NOME DOS PILOTOS DESIGNADOS>
# Histórico de transferências: <LISTAGEM DAS BASES PELAS QUAIS A AERONAVE PASSOU MOSTRANDO A DATA / HORA E BASE>

from datetime import datetime
class JatoMilitar2Lugares:
    def __init__(self, modelo, baseOrig):
        self.modelo = modelo
        self.baseOrig = baseOrig
        self.historico = [self.base]
        self.designa = False
    
    def designar_piloto(self, piloto, coPiloto):
        self.piloto = piloto
        self.coPiloto = coPiloto
        self.designa = True

    def rebasear_aeronave(self, baseNova):
        if self.designa:
            self.base = baseNova
            self.data = datetime.now().strftime('%d-%m-%Y')
            self.hora = datetime.now().strftime('%H:%M')
            self.historico.append([self.base, self.data, self.hora])
            self.designa = False
        
        else:
            return print("Não foi possível rebasear a aeronave pois não há piloto designado.")
    
    def __str__(self):
        return """ 
                Jato: %s
                Base de Origem: %s
                Histórico de Transferências: %s
                """ % (self.modelo, self.historico[0], self.historico[1::])

jato2 = JatoMilitar2Lugares('TT18', 'Maringá')
jato2.designar_piloto('Jakson Guimarães', 'Rodrigo Carvalho')
jato2.rebasear_aeronave('Rio de janeiro')
print(jato2)