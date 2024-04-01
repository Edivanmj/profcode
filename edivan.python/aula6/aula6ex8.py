import os
os.system ('cls')

nome = input ('Qual o seu nome?')
horas = int (input ('Que horas são (0-23)?'))

if horas>= 5 and horas<=12:
    print ('Bom dia')
elif horas>= 13 and horas<= 18:
    print ( 'Boa tarde')
else:
    print('Boa noite')