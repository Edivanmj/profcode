# Solicita os valores das contas ao usuário
conta_agua = float(input("Digite o valor da conta de água: R$"))
conta_luz = float(input("Digite o valor da conta de luz: R$"))
conta_telefone = float(input("Digite o valor da conta de telefone: R$"))

# Solicita o valor do salário ao usuário
salario = float(input("Digite o valor do seu salário: R$"))

# Calcula o total das contas
total_contas = conta_agua + conta_luz + conta_telefone

# Verifica se o salário é suficiente para pagar as contas
if salario >= total_contas:
    # Calcula o valor restante do salário após pagar as contas
    salario_restante = salario - total_contas
    print("Salário suficiente!")
    print(f"Valor restante do salário após pagar as contas: R${salario_restante:.2f}")
else:
    print("Salário insuficiente!")
