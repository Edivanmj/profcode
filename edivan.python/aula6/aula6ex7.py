import os
os.system ('cls')

pontox = float(input('Digite as cordenadas de x'))
pontoy = float(input('Digote as cordenadas de y'))

saida = pontox+pontoy

#1º quadrante: x>0 e y>0• 
#2º quadrante: x<0 e y>0• 
#3º quadrante: x<0 e y<0• 
#4º quadrante: x>0 e y<0



if pontox>0 and pontoy<0:
    q=1
elif pontox>0 and pontoy<0:
    q=2
elif pontox>0 and pontoy<0:
    q=3
else:
    q=4
    print(f'O valor p{pontox},{pontoy} pertence a {q}º quadrante')