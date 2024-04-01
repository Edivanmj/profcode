# Solicita os dois números reais ao usuário
numero1 = float(input("Digite o primeiro número real: "))
numero2 = float(input("Digite o segundo número real: "))

# Solicita a escolha da operação ao usuário
print("Escolha uma operação:")
print("1 - Média entre os números digitados")
print("2 - Diferença entre o maior e o menor número digitado")
print("3 - Produto entre os números digitados")
print("4 - Divisão do primeiro pelo segundo")

# Obtém a escolha do usuário
opcao = int(input("Digite o número da operação desejada: "))

# Verifica a escolha do usuário e executa a operação correspondente
if opcao == 1:
    media = (numero1 + numero2) / 2
    print(f"A média entre os números digitados é: {media} ")
elif opcao == 2:
    diferenca = abs(numero1 - numero2)
    print(f"A diferença entre o maior e o menor número digitado é: {diferenca}")
elif opcao == 3:
    produto = numero1 * numero2
    print(f"O produto entre os números digitados é: {produto}")
elif opcao == 4:
    if numero2 == 0:
        divisao = numero1 / numero2
        print(f"A divisão do primeiro pelo segundo é: {divisao}")
    else:
        print("Erro: o segundo número não pode ser zero para a divisão.")
else:
    print("Erro: Opção inválida.")

#def calcular_media(num1, num2):
#    return (num1 + num2) / 2
#
#def calcular_diferenca(num1, num2):
#    return abs(num1 - num2)
#
#def calcular_produto(num1, num2):
#    return num1 * num2
#
#def calcular_divisao(num1, num2):
#    if num2 == 0:
#        return None
#    return num1 / num2
#
#def main():
#    num1 = float(input("Digite o primeiro número real: "))
#    num2 = float(input("Digite o segundo número real: "))
#
#    print("Escolha a operação:")
#    print("1 - Média entre os números digitados")
#    print("2 - Diferença entre o maior e o menor número digitado")
#    print("3 - Produto entre os números digitados")
#    print("4 - Divisão do primeiro pelo segundo")
#
#    escolha = int(input("Digite o número da operação desejada: "))
#
#    if escolha == 1:
#        print("A média entre os números digitados é:", calcular_media(num1, num2))
#    elif escolha == 2:
#        print("A diferença entre o maior e o menor número digitado é:", calcular_diferenca(num1, num2))
#    elif escolha == 3:
#        print("O produto entre os números digitados é:", calcular_produto(num1, num2))
#    elif escolha == 4:
#        if num2 != 0:
#            print("A divisão do primeiro pelo segundo é:", calcular_divisao(num1, num2))
#        else:
#            print("Erro: Não é possível dividir por zero.")
#    else:
#        print("Erro: Opção inválida.")
#
#if __name__ == "__main__":
#    main()
#