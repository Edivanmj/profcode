import math, os

os.system('cls')
comp = float (input('Digite o comprimento da sombra em m'))
angulo = float(input('Qual o anguloo de enclinação em º:'))

angulo = math.radians(angulo)
h = comp * math. tan(angulo)
print(f'A altura do prédio é {h} metros')