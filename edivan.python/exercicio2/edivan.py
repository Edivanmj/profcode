# Solicita os valores dos lados do retângulo ao usuário
lado1 = float(input("Digite o valor do primeiro lado do retângulo: "))
lado2 = float(input("Digite o valor do segundo lado do retângulo: "))

# Calcula o perímetro do retângulo
perimetro = 2 * (lado1 + lado2)

# Calcula a área do retângulo
area = lado1 * lado2

# Mostra o perímetro e a área do retângulo
print("O perímetro do retângulo é:", perimetro)
print("A área do retângulo é:", area)
