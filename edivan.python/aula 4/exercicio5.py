import math, os

os.system('cls')

angulo = float(input(' Digite o ângulo em º'))
angulo = math.radians(angulo)

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tang = math.tag(angulo)

print(f'O seno é `{seno:.1f}')
print(f'O cosseno é {cosseno:.1f}')
print(f'A tangente é {tang:.1f}')