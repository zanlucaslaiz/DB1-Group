# Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 

print ('Analizando uma letra.')
n = str(input('Digite uma letra: ')).upper()

if n.isalpha():
  if n == 'A':
    print ('É uma vogal.')
  elif n == 'E':
    print ('É uma vogal.')
  elif n == 'I':
    print ('É uma vogal.')
  elif n == 'O':
    print ('É uma vogal.')
  elif n == 'U':
    print ('É uma vogal.')
  else:
    print ('É uma consoante.')
else:
  print ('Não é uma letra.')
