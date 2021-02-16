import math

massa = float(input('Massa >> '))
di = float(input("Deslocamento inicial >>  "))
df = float(input("Delocamento final >>  "))
ang = float(input("Algulo >>  "))

seno = math.sin(math.radians(ang))
a = ((massa)*(9.8)*(seno))

velocidadeQuadr = ((2*a)*(df - di))
velocidade = math.sqrt(velocidadeQuadr)

tempo = (velocidade/a)
#t = math.sqrt((2*df)/(a))


print('Aceleração = ',a, 'm/s^2')
print('Velocidade = ',velocidade, 'm/s')
print('Tempo = ', tempo, 's')
#print('Tempo = ', t, 's')
