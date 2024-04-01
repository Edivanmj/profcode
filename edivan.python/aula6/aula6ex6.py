n1 = float( input('Digite a primeira nota:'))
n2 = float( input ( 'digite a segun da nota:'))

#Média de Aproveitamento ConceitoEntre 9.0 e 10.0 A
#Entre 7.5 e 8.9 B
#Entre 6.0 e 7.4 C
#Entre 4.0 e 5.9 D
#Abaixo de 4.0 E

media = (n1+n2) /2

if media>= 9.0:
    print (' media A aprovado' )
elif media>= 7.5 and media<=8.9:
    print (' media B aprovado' )
elif media>= 6.0 and media<= 7.4:
    print ('media c aprovado')
elif media >=4.0 and media <= 5.9:
    print ('media D reprovado')
else:
    print ('media E resprovado')