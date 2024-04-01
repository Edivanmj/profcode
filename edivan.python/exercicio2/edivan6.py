# Solicita o valor do gasto ao cliente
valor_gasto = float(input("Digite o valor total do gasto no restaurante ComaBem: "))

# Calcula a gorjeta (10% do valor gasto)
gorjeta = 0.1 * valor_gasto

# Calcula o valor total a ser pago (gasto + gorjeta)
total_a_pagar = valor_gasto + gorjeta

# Exibe o valor total a ser pago
print("O valor total a ser pago, incluindo a gorjeta de 10%, é:", total_a_pagar)
