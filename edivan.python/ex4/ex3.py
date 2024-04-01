# Obtém o valor da compra do usuário
valor_compra = float(input("Digite o valor da compra: R$"))

# Verifica se a compra é maior que R$ 200
if valor_compra > 200:
    # Calcula o desconto de 20%
    desconto = 0.2 * valor_compra
    # Calcula o valor da compra com o desconto
    valor_compra_com_desconto = valor_compra - desconto
    print(f"Valor da compra com desconto: R${valor_compra_com_desconto:.2f} (desconto de 20%)")
else:
    # Exibe o valor da compra sem desconto
    print(f"Valor da compra: R${valor_compra:.2f} (sem desconto)")
