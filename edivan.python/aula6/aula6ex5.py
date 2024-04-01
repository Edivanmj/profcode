import math

area = int (input('Digite a area a ser pintada (em m²)'))
litros = area/3
latas =  math.ceil (litros/18)

valor = latas * 80
print(f'Você precisara de{latas} latas')
print(f'total a pagar R$ {valor}')

