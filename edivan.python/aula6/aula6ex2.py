import os
os.system ('cls')

segundos= int (input(' digite os segundos:'))
horas = segundos // 3600
minutos= segundos % 3600 //60
segundos = segundos % 60

print (f'{horas}: {minutos}:{segundos}:')