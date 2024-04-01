import math

# Solicita os coeficientes da equação
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calcula o discriminante
delta = b**2 - 4*a*c

# Verifica se as raízes são reais
if delta >= 0:
    # Calcula as raízes
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    # Exibe as raízes
    print("As raízes da equação são:", x1, "e", x2)
else:
    print("A equação não possui raízes reais.")
