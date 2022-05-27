# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.

print ('Vamos calcular o salário com reajuste') 
salario = float(input('Digite o salário atual do funcionário: '))
reajuste = float(input('Digite a porcentagem do reajuste,somente numero."exemplo: 15 "'))
r = salario + salario * reajuste / 100
print (f'O salário reajustado é {r}.')