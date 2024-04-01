import os 
os.system('cls')
placa = int(input('infome sua placa:'))
final = placa%10
match(placa):
 case 1|2:
  print('O veiculo não pode circular ás segundas-feiras')
 case 3|4:
  print('O veiculo não pode circular ás terça-feiras')
 case 5|6:
  print('O veiculo não pode circular ás Quarta-feiras')
 case 7|8:
  print('O veiculo não pode circular ás Quinta-feiras')
 case 9|0:
  print('O veiculo não pode circular ás sexta-feiras')
 case _:
  print('dados invalido')
  