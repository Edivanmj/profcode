valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 200:
    desconto = valor_compra * 0.20
    valor_com_desconto = valor_compra - desconto
    print(f"Valor da compra com desconto de 20%: R$ {valor_com_desconto}")
else:
    print(f"Valor da compra: R$ {valor_compra}")