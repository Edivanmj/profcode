peso = float(input('iforme o peso:'))
altura = float(input('informe a aultura:'))
imc = peso/ altura **2
if imc <20:
    print(f'seu imc e {imc} Você esta abaixo do peso')
elif imc <25 :
    print(f'você esta {imc} normal')
elif imc <30 :
    print(f'você esta gordo {imc}')
else: 
    print(f'você esta extraordinariamente balofo vai se trata!! {imc}')
