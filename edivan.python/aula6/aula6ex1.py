import os
os. system ('cls')

salario = float(input('informe seu salrio:'))
vendas = float(input('Digite a quantidade de vendas:'))

comissao= salario * 4/100
salario += comissao

print(f'comissão: R$ {comissao}')
print(f'salario: R$ {salario}')

