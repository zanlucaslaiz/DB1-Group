# Faça um programa para a leitura da duas notas parciais de um aluno. O programa deve calcular a média alcançada pelo aluno e apresentar. A mensagem “aprovado” , se a média alcançada for maior ou igual a sete; a mensagem “reprovado”, se a média for menor do que sete e a mensagem “aprovado com distinção”, se a média for igual a dez.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 70 and media != 100:
  print ('Você foi Aprovado.')
if media < 70:
  print ('Você foi Reprovado.')
if media == 100:
  print ('Você foi Aprovado com distinção.')
