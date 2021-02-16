import math

massaA = float(input('Massa de A: '))
massaB = float(input('Massa de B: '))
Theta = float(input('Angulo Theta: '))
Beta = float(input('Angulo Beta: '))
g = float(input('Gravidade: '))


senoTheta = math.sin(math.radians(Theta))
senoBeta = math.sin(math.radians(Beta))

Pax = ((massaA)*(g)*(senoTheta))
Pbx = ((massaB)*(g)*(senoBeta))

if Pax < Pbx:
    a = (((((massaB)*(senoBeta)) - ((massaA)*(senoTheta)))*(g))/(massaA + massaB))
    print('Aceleração = ', a, 'm/s^2')
    t = ((((-1)*(massaB))*((((massaB)*(senoBeta)) - ((massaA)*(senoTheta))))/(massaA + massaB)) + ((massaB)*(g)*(senoBeta)))
    print('Tração = ',t, 'N')
    print('entrou no 1')

elif Pax > Pbx:
    a = (((((massaA)*(senoTheta)) - ((massaB)*(senoBeta)))*(g))/(massaA + massaB))
    print('Aceleração = ', a, 'm/s^2')
    t = (((-1)*(massaA))* (2.544)) + ((massaA)*(g)*(senoTheta))
    print('Tração = ',t, 'N')
    print('entrou no 2')
    
else:
    a = 0
    print('Aceleração = ', a, 'm/s^2')
    t = massaA*g*senoTheta    
    print('Tração = ',t, 'N')
    print('entrou no 3')



#t = ((((-1)*(massaB))*((((massaB)*(senoBeta)) - ((massaA)*(senoTheta))))/(massaA + massaB)) + ((massaB)*(g)*(senoBeta)))

#print('Aceleração = ', a, 'm/s^2')
#print('Tração = ',t, 'N')
