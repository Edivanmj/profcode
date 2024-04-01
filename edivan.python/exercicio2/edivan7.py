# Solicita a temperatura em Celsius ao usuário
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converte para Fahrenheit
temperatura_fahrenheit = (9/5) * temperatura_celsius + 32

# Converte para Kelvin
temperatura_kelvin = temperatura_celsius + 273.15

# Exibe as temperaturas convertidas
print("Temperatura em Fahrenheit:", temperatura_fahrenheit, "°F")
print("Temperatura em Kelvin:", temperatura_kelvin, "K")
