# Solicita a cotação do dólar ao usuário
cotacao_dolar = float(input("Digite a cotação do dólar (em reais): "))

# Solicita o valor em dólares ao usuário
valor_dolar = float(input("Digite o valor em dólares: "))

# Converte o valor de dólares para reais
valor_reais = valor_dolar * cotacao_dolar

# Exibe o valor equivalente em reais
print("O valor equivalente em reais é:", valor_reais, "R$")
