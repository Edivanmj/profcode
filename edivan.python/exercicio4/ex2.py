
turno = input('Digite seu turno de trabalho(D para diuno ou N para noturno):')
horas= float (input('Digite suas horas trabalhadas:'))

if turno == 'N' or 'n':
    valor_horas = 45.00
    
else:
    valor_horas = 37.50
    
salario = horas * valor_horas
    
print(f"O valor do salário é R$ {salario}")   
