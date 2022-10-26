# Criar um método rebasear_aeronave, que deverá receber de parâmetro o nome da base para onde a aeronave deverá ser enviada.
# Antes de registrar, é necessário validar se o piloto foi designado para a aeronave, e somente se houver piloto, 
# registrar a informação de rebaseamento, a data e hora que a movimentação foi realizada, deverá ser registrada também.
# Sobrescreva o métod __str__ da classe, para imprimir o seguinte conteúdo:
# Jato: <NOME DA AERONAVE>
# Base inicial: <NOME DA BASE DE ORIGEM>
# Piloto: <NOME DO PILOTO DESIGNADO>
# Histórico de transferências: <LISTAGEM DAS BASES PELAS QUAIS A
# AERONAVE PASSOU MOSTRANDO A DATA / HORA E BASE>

from datetime import datetime
class JatoMilitar1Lugar:
    def __init__(self, modelo, baseOrig):
        self.modelo = modelo
        self.baseOrig = baseOrig
        self.historico = [self.base]
        self.designa = False
    
    def designar_piloto(self, piloto):
        self.piloto = piloto
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

jato1 = JatoMilitar1Lugar('TT18', 'Maringá')
jato1.designar_piloto('Jakson Guimarães')
jato1.rebasear_aeronave('Rio de janeiro')
print(jato1)