#Faça um programa em python que solicite um caractere ao usuário
#e imprima se é uma vogal

import math, os 
os.system ('cls')

c= input('Digite uma caractere:')

#if c == 'a' or c== 'e' or c== 'i' or c== 'o' or c== 'u':
if c in 'aeiou':
 print(f'{c} é uma vogal')
else:
 print(f'{c} não é uma vogal')

