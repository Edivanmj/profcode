a = float (input(' Digite sua altura:'))
x = input('Digite seu sexo M masculino F feminino:')

if x == 'm' or x == 'M':
    resultado = 72.7* a - 58
else:
    resultado = 62.1* a - 44.7
    print(f'peso indeal = {resultado}:.2f')