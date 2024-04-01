import os
os. system('cls')
import math
num = float (input('Digite um número real'))

absoluto = math.fabs(num)
inteiro = math.trunc(absoluto)
raiz = math.sqrt(absoluto)

fatorial = math.factorial (inteiro)

print(f'a) {absoluto}')
print(f'b) {inteiro}')
print(f'c) {raiz:1f}')
print(f'd){fatorial}')