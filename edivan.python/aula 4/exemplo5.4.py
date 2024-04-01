import os
os.system('cls')



nome = input('Qual o seu nome')
nota1 = float (input("Digite a primeira nota"))
nota2 = float (input("Digite a segunda nota"))
media = (nota1 + nota2)/2

#if media >= 6.0:
    #print(f'Parabéns {nome}, vocé foi aprovado')
#else:
    #print(f'')

result = ' aprovado' if media >= 6.0 else 'reprovado'
print(f'Olá {nome}, você foi {media}')