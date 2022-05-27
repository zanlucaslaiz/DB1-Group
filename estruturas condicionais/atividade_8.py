# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
# PS: digite 'import math' no início de seu script. Para achar a raiz quadrada da variável x, faça: math.sqrt(x)

import math

print('Equação de segundo grau ax² + bx + c.')
a = float(input('Digite o coeficiente a: '))
a = math.sqrt(a)
if a == 0:
    print('O coeficiente deve ser diferente de zero quaso contrario não é uma equação de segundo grau.')
else:
    b = float(input('Digite o coeficiente b: '))
    c = float(input('Digite o coeficiente c: '))
    delta = b*b - (4*a*c)
    if delta<0:
      print ('Delta menor que 0. Raizes imaginárias. Tchau')
    elif delta == 0:
      raiz = -b / (2*a)
      print ('Delta=0 , raiz = ',raiz)
    else:
      raiz1 = (-b + math.sqrt(delta) ) / (2*a)
      raiz2 = (-b - math.sqrt(delta) ) / (2*a)
      print (f'Raizes: {raiz1:.2} e {raiz2:.2}')
