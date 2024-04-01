import os
os.system ('cls')

print('[S] Simples\n[D] Duplo\n[T]Triplo')
tipo = input('Digite uma opção: ')
qte = int(input('Digite a quantidade de diarias: '))

if tipo in 'sSdDtT':
    print('Opção invalida!!')
    qtd = int (input('Digite a quantidade de diaria: '))

    if tipo in 'sS':
        print(f'O valor total  pago sera? {qtd * 255.50}')