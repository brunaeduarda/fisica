import math

massa1 = float(input('Massa 1: '))
massa2 = float(input('Massa 2: '))
angulo = int(input('Angulo: '))
forçaHorz = float(input('Força horizontal: '))

seno = math.sin(math.radians(angulo))

g = 9.8
a = ((((massa2)*(g)*(seno)) + (forçaHorz))/(massa1 + massa2))

af = (g*seno)

tenção = (((massa1)*(a))-(forçaHorz))

f = ((massa1)*(af))

print('Aceleração = ',a, 'm/s^2')
print('Tençao = ', tenção,'N')
print('Modulo da Força que a corda pode assumir sem que fique frouxa: ',f,'N')
#print('Tu ta usando essa: ',af)
