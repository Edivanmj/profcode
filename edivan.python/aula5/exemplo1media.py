import os
os.system('cls')

nome = input('Qual o nome do aluno:')
nota = float(input(f'Digite a frequecia do  {nome}:'))
freq = int(input(f'Digite a frequencia do {nome}:'))

if freq < 75:
    print(f'{nome} você foi reprovado por frequencia!!')
elif nota < 3:
        print(f'Que pena! {nome} você foi reprovado por nota')
elif nota < 6:
            print(f'{nome} você esta de exame final')
else:
    print(f'parabéns {nome} você foi aprovado')