# Faça um Programa que pergunte em que turno você estuda


turno = str(input('Qual turno você estuda? \nM - Matutino, V - Vespertino, N - Noturno.')).upper()

if turno.isalpha():
    if turno == 'M':
        print('Bom Dia!')
    elif turno == 'V':
        print('Boa Tarde!')
    elif turno == 'N':
        print('Boa Noite!.')
    else:
        print('Valor invalido!')

  
