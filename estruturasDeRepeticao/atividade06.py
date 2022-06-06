# Faça um programa para o cálculo de uma folha de pagamento.
# nesse exercicio estou considerando que o funcionário ganha R$3000,00. 
print('ZanlucasME \nFolha de pagamento.')
colaborador = str(input('Digite o nome do colaborador: '))
sb = float(input('Digite o salário bruto do colaborador: '))
fgts = sb * 8 / 100
inss = sb * 11 / 100
irrf = 61.40
vt = sb * 6 / 100
va = sb * 10 / 100
dt = fgts + inss + irrf + vt + va
sl = sb - dt

print (f'Colaborador(a): {colaborador}.')
print (f'Salário Bruto:{sb}')
print (f'Descontos:\nFGTS: R${fgts}\nINSS: R${inss}\nIRRF: R${irrf}\nVT: R${vt}\nVA: R${va}')
print (f'Total descontado:  R${dt}')
print (f'Salário liquido: R${sl}')

