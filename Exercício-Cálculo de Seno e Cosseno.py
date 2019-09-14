from math import hypot

co = float(input('Digite o comprimento do cateto oposto:\n'))
ca = float(input('Digite o comprimento do cateto adjacente:\n'))
hy = hypot(co, ca)

print('A hipotenusa vai medir: {:.2f}'.format(hy))