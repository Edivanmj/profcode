# Solicita o salário atual ao usuário
salario_atual = float(input("Digite o salário atual: "))

# Calcula o valor da comissão (5% do salário atual)
comissao = salario_atual * 0.05

# Calcula o novo salário (salário atual + comissão)
novo_salario = salario_atual + comissao

# Mostra o novo salário com a comissão adicionada
print("O novo salário com 5% de comissão é:", novo_salario)
