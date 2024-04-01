import os
os.system('cls')
compra = float(input('Qua o valor da compra?'))
parcela = int(input('informe a quantidade de parcela 2 | 4 | 6 | 8'))
if parcela == 2: juros =3/100
elif parcela ==4: juros = 7/100
elif parcela ==6: juros= 9/100
elif parcela ==8 : juros = 12/100
else: juros = -1

#match(parc):
#case 2:
#juros = 3/100
#case e juros fucina repetidamente

if juros == -1:
    print('Opção de parcelamento invalida')
else:
    total = compra + compra*juros
    print(f'Cada parcela sera de R${total/parcela}')

    
