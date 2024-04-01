import os, math
os.system('cls')

num = float(input('Digite um número positivo'))

if num >=0:
    raiz = math.sqrt(num)
    print(f'A raiz de {num} é {raiz:.2f}')
else:
    print(f'Não tem raiz quadrada de numero negativo!')
