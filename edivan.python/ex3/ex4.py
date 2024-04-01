# Solicita os valores ao usuário
valor_prestacao = float(input("Digite o valor da prestação: "))
multa = float(input("Digite a porcentagem de multa pelo atraso (%): "))
qtde_dias = int(input("Digite a quantidade de dias de atraso: "))

# Calcula o valor da prestação atualizado
prestacao_atualizada = valor_prestacao + (valor_prestacao * (multa / 100) * qtde_dias)

# Exibe o valor da prestação atualizado
print("O valor da prestação atualizado é:", prestacao_atualizada)
