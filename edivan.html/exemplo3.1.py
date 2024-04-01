import os
import math,os

os.system('cls')
raio = float(input('Digite o raio em cm: '))

area = math.pi * raio**2
comprimento = 2 * math.pi * raio

print(f'A área do circuito é: {area} cm²')
print(f'O comprimento da circunferencia é: {comprimento:2f}')