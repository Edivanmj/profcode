# Solicita os valores ao usuário
altura_tronco = float(input("Digite a altura do tronco da pirâmide (h): "))
base_menor = float(input("Digite o valor da base menor (Bmenor): "))
base_maior = float(input("Digite o valor da base maior (Bmaior): "))

# Calcula o volume do tronco da pirâmide
volume = altura_tronco / 3 * (base_maior**2 + base_menor**2 + (base_maior**2 * base_menor**2)**0.5)

# Exibe o resultado
print("O volume do tronco da pirâmide é:", volume)
