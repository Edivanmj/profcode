# Solicita a idade ao usuário
anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite o número de meses: "))
dias = int(input("Digite o número de dias: "))

# Calcula a idade total em dias
idade_em_dias = anos * 365 + meses * 30 + dias

# Exibe a idade total em dias
print("Sua idade expressa apenas em dias é:", idade_em_dias, "dias.")
